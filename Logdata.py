import re
def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
    
        # YOUR CODE HERE
        log_list = []
        
        regexpattern = "(\d{1,4}\.\d{1,3}\.\d{1,3}\.\d{1,3})( - .* )(\[\d{2}\/\w{3}\/\d{4}\:\d{2}\:\d{2}\:\d{2}\s\-\d{4}\])( \".*?\")"
        
        for item in re.finditer(regexpattern, logdata):
            
            log_dict = {}
            log_dict["host"] = item.group(1)
            log_dict["user_name"] = item.group(2).replace(' - ','').replace(' ','')
            log_dict["time"] = item.group(3).replace('[','').replace(']','')
            log_dict["request"] = item.group(4).replace(' "',"").replace('"',"")
            log_list.append(log_dict)
        
        return log_list
