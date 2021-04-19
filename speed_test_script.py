import speedtest
st = speedtest.Speedtest()

option = int(input("1 - Download\n2 - Upload\n3 - Ping\n"))

if option == 1:
    print(st.download())
elif option == 2:
    print(st.upload())
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print("Please enter a valid option")