# def solution(s):
#     total_length = len(s)
#     if total_length < 1 or total_length > 100:
#         raise Exception("The length should be between 1-100")
    
#     mid_length = int(total_length / 2)
#     end_pos = total_length - 1

#     output_str = ""
#     for i in range(mid_length):
#         output_str += s[i]
#         output_str += s[end_pos - i]

#     if total_length % 2 != 0:
#         output_str += s[mid_length]

#     return output_str

def get_next_available(mins, trip):
    for avail in trip:
        if avail >= mins:
            if(avail > 2000):
                raise Exception("error")
            return avail

def solution(a2b, b2a, trips):
    a2b_len = len(a2b)
    b2a_len = len(b2a)

    if a2b_len < 1 or a2b_len > 100 or b2a_len < 1 or b2a_len > 100:
        raise Exception("Error")

    is_first = True
    total = 0
    for i in range(trips):
        if is_first:
            start_mins = a2b[0]
            if start_mins > 2000:
                raise Exception("Error")
            total = start_mins
            is_first = False
        else:
            next_avail = get_next_available(total, a2b)
            total = next_avail
        total += 100
        next_avail = get_next_available(total, b2a)
        total = next_avail

    if total + 100 > 2000:
        raise Exception("error")
    
    return total + 100


def process_servers(servers, worklimit, recoveryTime):
    for server_cnt in range(len(servers.keys())):
        if servers[server_cnt] < worklimit:
            servers[server_cnt] += 1
            if servers[server_cnt] == worklimit:
                servers[server_cnt] = recoveryTime
            break

    return servers

def solution(nServers, worklimit, recoveryTime, events):
    servers = {}
    for cnt in range(nServers):
        servers[cnt] = 0
    
    for event in events:
        if event == "REQUEST":
            process_servers(servers, worklimit, recoveryTime)
        elif "UP" in event:
            server_num = int(event.split(" ")[1])
            servers[server_num - 1] = 0

        





# print(solution([0,200,500], [99, 210, 450], 1))

# print(solution("abcde"))
