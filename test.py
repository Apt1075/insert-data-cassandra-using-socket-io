import telnetlib

host = "tp1.itrackrtd.co.in"
port = 9004

try:
    tn = telnetlib.Telnet(host, port, timeout=10)
    tn.write(b'Your command\n')
    response = tn.read_until(b'expected_output', timeout=10)
    print(response.decode('utf-8'))
    tn.close()
except Exception as e:
    print(f"Error: {e}")

