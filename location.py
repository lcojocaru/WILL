def do_rss_stack_diff(ssid_dict):
    ssid_dict_diff = {}
    for ssid in ssid_dict:
        diff = 0
        for ssid_iter in ssid_dict:
            diff += abs(ssid_dict[ssid] - ssid_dict[ssid_iter])
        ssid_dict_diff[ssid] = diff
    return ssid_dict_diff