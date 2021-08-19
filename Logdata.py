import re
def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
    
        # YOUR CODE HERE
        log_list = []
        log_dict = {}
        regexpattern = "(\d{1,4}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        regexpattern2 = "\s-\s\w+"
        for item in re.findall(regexpattern, logdata):
            
            #log_dict = {}
            log_dict["host"] = item
            log_list.append(log_dict)
        
        for item2 in re.findall(regexpattern2, logdata):

            log_dict["user_name"] = item2
            log_list.append(log_dict)
            log_dict["time"] = item.group(3)
            #log_dict["request"] = item.group(4)
        
        return log_list
