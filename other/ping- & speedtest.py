"""
Speedtests & Pingtests by (c)2025 Justus Decker
"""

from ping3 import ping #pip install ping3
import speedtest #pip install speedtest-cli
from sys import argv

def colt(text:str,color:str="31"):
    """
    Get Colorful Text. For more information visit: 
    https://gist.githubusercontent.com/fnky/458719343aabd01cfb17a3a4f7296797/raw/9363ac8dd0aa6ef00a85b042f62227395ef67ae2/ANSI.md
    View section: 8-16 Colors!
    """
    return f"\033[{color}m{text}\033[0m"

class internet_tests:
    def __init__(self,
                 ips_to_check : list[str] = ["8.8.8.8","google.com"],
                 package_size : int = 32,
                 pings : int = 100) -> None:
        self.ips = ips_to_check
        self.package_size = package_size
        self.pings = pings
    def get_statistics(self,current,ip_adress,results):
        print(f"\033[2J[{colt(f'{int((current+1)/self.pings*100)}%',36)}] [{colt(current+1,36)} / {colt(self.pings,36)}] Answer from: ({colt(ip_adress,33)}) cur: {colt('TIMEOUT' if results[ip_adress][-1] >= 1000 else results[ip_adress][-1],31 if results[ip_adress][-1] >= 1000 else 32)} ms min: {colt(min(results[ip_adress]),32)} ms max: {colt(max(results[ip_adress]),32)}\033[0m ms avg: {colt(sum(results[ip_adress])//len(results[ip_adress]),32)} ms")
    
    def ping_test(self):
        results = {}
        for ip_adress in self.ips:
            timeouts = 0
            results[ip_adress] = []
            
            for _ in range(self.pings):
                current_ping = ping(dest_addr=ip_adress,size=self.package_size,timeout= 1,unit="ms")
                if current_ping is None:
                    
                    results[ip_adress].append(1000)
                    self.get_statistics(_,ip_adress,results)
                    timeouts += 1
                    continue
                
                results[ip_adress].append(int(current_ping))

                self.get_statistics(_,ip_adress,results)
        self.get_full_statistics(results)
    def get_full_statistics(self,results:dict):
        print('\033[2J',end="")
        for key in results:
            timeouts = results[key].count(1000)
            min_ping = min(results[key])
            max_ping = max(results[key])
            avg = sum(results[key])//len(results[key])
            ip_f = ' '*(int(18/2)-int(len(key)/2))
            print(f"""
    ┌─────────┬──────────────────┐
    │ Result: │{key:^18}│
    ├────┬────┼───┬─────┬────────┘
    │send│{str(self.pings):<4}│min│{str(min_ping):<5}│
    │okay│{str(self.pings - timeouts):<4}│max│{str(max_ping):<5}│
    │loss│{str(timeouts):<4}│avg│{str(int(avg)):<5}│
    └────┴────┴───┴─────┘
        """)
    def speed_test(self):
        test = speedtest.Speedtest()
        print("Loading Serverlist...")
        test.get_servers()
        print("Choosing best Server...")
        best = test.get_best_server()
        print(f"Found: {colt(best['host'],34)} located in {colt(best['country'],36)} latency: {colt(best['latency'],32)} ms")
        print("Performing Download Test...")
        down_result = test.download()
        print("Performing Upload Test...")
        up_result = test.upload()
        print("Performing Ping Test...")
        ping_result = test.results.ping
        print(f"""
    ┌──────────┬──────────┬──────┐
    │  upload  │ download │ ping │
    │{f'{up_result / 1024 / 1024:.2f}':<10}│{f'{down_result / 1024 / 1024:.2f}':<10}│{f'{ping_result:.2f}':<6}│
    └──────────┴──────────┴──────┘
        """)
def check_arguments():
    PT = internet_tests()
    if not argv[1:]:
        PT.ping_test()
    for arg in argv[1:]:
        match arg:
            case '-st':
                PT.speed_test()
            case '-pt':
                PT.ping_test()

if __name__ == "__main__":
    check_arguments()


