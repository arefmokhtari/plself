#                   [   Plague Dr.  ]
from speedtest import Speedtest
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
async def dict_speedtest() -> dict:
    st = Speedtest()
    st.get_servers()
    st.get_best_server()
    st.download()
    st.upload()
    return st.results.dict()
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #