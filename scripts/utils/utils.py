import base64
import json
import struct
from time import perf_counter_ns
from typing import List, Any, Dict, Union, Tuple, Set

from pytgcalls.exceptions import GroupCallNotFound
from pytgcalls.types.groups.group_call import GroupCall
from telethon.tl.types import Channel


def cx(callback, *args):
    """
    calculate execution time of a function
    :param callback: function to be executed
    :param args: arguments to be passed to the function
    :return: (result of the function, execution time in milliseconds)
    """
    t1 = perf_counter_ns()
    result = callback(*args)
    t2 = perf_counter_ns()
    t = (t2 - t1) / 1000000
    return result, t


def get_exact_link(link):
    """
    get exact link from link (if redirected)
    :param link: link to be checked
    :return: exact link
    """
    import requests
    r = requests.head(link)
    location = r.headers.get('location')
    return link if location is None else location


class Attrify(dict):
    """Custom dict to access dict keys as attributes."""

    def __init__(self, *args, **kwargs):
        """
        Convert normal dict to Attrified-Dict, So you can access dict keys as attributes.
        Can also convert nested structures.
        Example:
            >>> resp = {"quota": 100}
            >>> resp = Attrify(resp)
            >>> resp.quota
            100
            >>> resp["quota"]
            100
            >>> nested_resp = {"quota": {"limit": 100, "expires_at": 12345}}
            >>> nested_resp = Attrify(nested_resp)
            >>> nested_resp.quota.limit
            100
            >>> nested_resp.quota.expires_at
            12345
            >>> complex_nested_resp = {"data": {"results": [{"name": "something"}, {"name": "anything"}]}}
            >>> complex_nested_resp = Attrify(complex_nested_resp)
            >>> complex_nested_resp.data.results[0].name
            something
        Notes:
            1. If both args and kwargs are given, args[0] will be preffered
            2. Tuples and Sets are converted to List during conversion
        """
        if args:
            cdict = args[0]
        else:
            cdict = kwargs
        for key in cdict:
            if isinstance(cdict[key], dict):
                cdict[key] = Attrify(cdict[key])
            elif isinstance(cdict[key], (list, tuple, set)):
                cdict[key] = self.convert_list(cdict[key])
        super().__init__(*args, **cdict)

    def convert_list(self, n: Union[List[Any], Tuple[Any, ...], Set[Any]]) -> List[Any]:
        """Check list to see If there Is any list Inside it and If there is Attrify it."""
        new_list = []
        for item in n:
            if isinstance(item, (list, tuple, set)):
                new_list.append(self.convert_list(item))
            elif isinstance(item, dict):
                new_list.append(Attrify(item))
            else:
                new_list.append(item)
        return new_list

    def to_dict(self) -> Dict[str, Any]:
        """Convert Attrify back to dict."""
        _dict = dict(self)
        for key in _dict:
            if isinstance(_dict[key], Attrify):
                _dict[key] = _dict[key].to_dict()
            elif isinstance(_dict[key], (list, tuple, set)):
                new_list = []
                for i in _dict[key]:
                    if isinstance(i, Attrify):
                        new_list.append(i.to_dict())
                    else:
                        new_list.append(i)
                _dict[key] = new_list
        return _dict

    def prettify(self, indent: int = 4) -> str:
        """Shortuct for `json.dumps(output.to_dict(), indent = 4, ensure_ascii = False)`."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def __getattr__(self, attr) -> Any:
        """Return self[attr]."""
        if attr in self:
            return self[attr]
        raise AttributeError(f"Attrify has no attribute '{attr}'")

    def __dir__(self) -> List[str]:
        """Returns list of all attributes and keys that are alphabetic."""
        l = dict.__dir__(self)
        # Add all keys that are alphabetic.
        l.extend([x for x in self.keys() if str(x).isalpha()])
        return


def unpackInlineMessage(inline_message_id: str):
    temp = {}
    dc_id, message_id, chat_id, query_id = struct.unpack(
        '<iiiq',
        base64.urlsafe_b64decode(
            inline_message_id + '=' * (len(inline_message_id) % 4),
        ),
    )
    temp['dc_id'] = dc_id
    temp['message_id'] = message_id
    temp['chat_id'] = int(str(chat_id).replace('-1', '-1001'))
    temp['query_id'] = query_id
    temp['inline_message_id'] = inline_message_id
    return Attrify(temp)


class VcInfo:
    def __init__(self, call: GroupCall, chat: Channel):
        self.call = call
        self.chat = chat

    def call_exists(self):
        return True if self.chat.call_active else False

    def call_is_empty(self):
        return True if not self.chat.call_not_empty else False

    def joined(self):
        if self.call_exists():
            try:
                self.call.is_playing
                return True
            except GroupCallNotFound:
                return False

        else:
            return False

    def status(self):
        if self.call_exists():
            try:
                return self.call.status
            except GroupCallNotFound:
                return None
        else:
            return None

    def is_playing(self):
        if self.call_exists():
            try:
                return self.call.is_playing
            except GroupCallNotFound:
                return False
        else:
            return False
