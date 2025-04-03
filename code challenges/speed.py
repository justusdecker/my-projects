"""
(c) Masterschool

(c) 2025 rewritten by Justus Decker


import requests
from time import perf_counter

HTTP_RESPONSES = {
    200: ('OK', 'Request fulfilled, document follows'),
    301: ('Moved Permanently', 'Object moved permanently -- see URL list'),
    302: ('Found', 'Object moved temporarily -- see URL list'),
    403: ('Forbidden',
          'Request forbidden -- authorization will not help'),
    500: ('Internal Server Error', 'Server got itself in trouble')
}

class Speedtest:
    def __init__(self):
        pass
    def get_number_of_websites(self):
        num_websites = input("Enter the number of websites you want to rate: ")
        return int(num_websites) if num_websites.isdecimal() else 1
    
    def get_multiple_url_inputs(self,num_websites):
        urls = []
        for i in range(num_websites):
            url = ""
            while not self.check_url(url):
                url = input(f"Please enter the URL of website {i+1}: ")
            urls.append(url)
        return urls
    def measure_response_time(self,url):
        start_time = perf_counter()
        try:
            response = requests.get(url)
            end_time = perf_counter()
            if response.status_code in HTTP_RESPONSES:
                print("Got response: ", HTTP_RESPONSES.get(response.status_code,f"Unknown status code: {response.status_code}"))
            
        except Exception as E:
            print("Website dont exist!")
        end_time = perf_counter()
        return end_time - start_time
    def check_url(self,url:str):
        return url.startswith("https://") and url
    def main(self):
        num_websites = self.get_number_of_websites()
        urls = self.get_multiple_url_inputs(num_websites)
        response_times = [(url,self.measure_response_time(url)) for url in urls]
        sorted_response_times = sorted(response_times, key=lambda x: x[1])
        sorted_response_times = sorted_response_times[:3]
        print(f"Top {len(sorted_response_times)} speed ranking")
        for idx,data in enumerate(sorted_response_times):
            print(f"{idx}. {data[0]} - {data[1]*1000:.2f} ms")
        only_response_times = [response_time[1] for response_time in response_times]
        print(f"Average speed: {sum(only_response_times) / len(only_response_times)}")
Speedtest().main()
"""

import requests
from time import perf_counter

HTTP_RESPONSES = {
    200: ('OK', 'Request fulfilled, document follows'),
    301: ('Moved Permanently', 'Object moved permanently -- see URL list'),
    302: ('Found', 'Object moved temporarily -- see URL list'),
    403: ('Forbidden',
          'Request forbidden -- authorization will not help'),
    500: ('Internal Server Error', 'Server got itself in trouble')
}

class Speedtest:
    def __init__(self):
        pass
    def get_number_of_websites(self):
        num_websites = input("Enter the number of websites you want to rate: ")
        return int(num_websites) if num_websites.isdecimal() else 1
    
    def get_multiple_url_inputs(self,num_websites):
        urls = []
        for i in range(num_websites):
            url = ""
            while not self.check_url(url):
                url = input(f"Please enter the URL of website {i+1}: ")
            urls.append(url)
        return urls
    def measure_response_time(self,url):
        start_time = perf_counter()
        try:
            response = requests.get(url)
            end_time = perf_counter()
            if response.status_code in HTTP_RESPONSES:
                print("Got response: ", HTTP_RESPONSES.get(response.status_code,f"Unknown status code: {response.status_code}"))
            
        except Exception as E:
            print("Website dont exist!")
        end_time = perf_counter()
        return end_time - start_time
    def check_url(self,url:str):
        return url.startswith("https://") and url
    def main(self):
        num_websites = self.get_number_of_websites()
        urls = self.get_multiple_url_inputs(num_websites)
        response_times = [(url,self.measure_response_time(url)) for url in urls]
        sorted_response_times = sorted(response_times, key=lambda x: x[1])
        sorted_response_times = sorted_response_times[:3]
        print(f"Top {len(sorted_response_times)} speed ranking")
        for idx,data in enumerate(sorted_response_times):
            print(f"{idx}. {data[0]} - {data[1]*1000:.2f} ms")
        only_response_times = [response_time[1] for response_time in response_times]
        print(f"Average speed: {sum(only_response_times) / len(only_response_times)}")
Speedtest().main()