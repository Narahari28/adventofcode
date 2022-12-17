def max_flow(dests, flows, time, start):
    on = {}
    seen_states = {}
    per = 0
    total = 0
    for key in flows.keys():
        if flows[key] == 0:
            on[key] = True
    file = open('output.txt', 'a')
    ans = max_flow_helper(dests, flows, time, start, on, per, total, seen_states, file)
    file.close()
    return ans

def max_flow_helper(dests, flows, time, cur, on, per, total, seen_states, file):
    file.write(str(time) + " " + str(cur) + " " + ",".join(on.keys()) + " " + str(per) + " " + str(total) + "\n")
    seen_states["_".join(on.keys()) + " " + cur] = time
    if time == 0:
        file.write("Base case" + "\n")
        return total
    if len(on) == len(dests):
        file.write("Terminal case" + "\n")
        return total + per * time
    else:
        best = total + per * time
        if not cur in on:
            on[cur] = True
            best = max(best, max_flow_helper(dests, flows, time - 1, cur, on, per + flows[cur], total + per, seen_states, file))
            del on[cur]
        for candidate in dests[cur]:
            next_state = "_".join(on.keys()) + " " + candidate
            if not next_state in seen_states or seen_states[next_state] < time - 1:
                best = max(best, max_flow_helper(dests, flows, time - 1, candidate, on, per, total + per, seen_states, file))
        file.write("Returning best: " + str(best) + " " + str(time) + " " + str(cur) + " " + ",".join(on.keys()) + " " + str(per) + " " + str(total) + "\n")
        return best


def max_flow_double(valves, dests, flows, time, start):
    on = {}
    seen_states = {}
    per = 0
    total = 0
    for key in flows.keys():
        if flows[key] == 0:
            on[key] = True
    file = open('output.txt', 'a')
    ans = max_flow_helper_2(valves, dests, flows, time, start, start, on, per, total, seen_states, file)
    file.close()
    return ans

def max_flow_helper_2(valves, dests, flows, time, cur, cur2, on, per, total, seen_states, file):
    if len(seen_states) % 100000 == 0:
        print(len(seen_states), flush=True)
    # file.write(str(time) + " " + str(cur) + " " + str(cur2) + " " + ",".join(on.keys()) + " " + str(per) + " " + str(total) + "\n")
    key_rep = ""
    for valve in valves:
        if valve in on:
            key_rep = key_rep + "1"
        else:
            key_rep = key_rep + "0"
    seen_states[key_rep + " " + cur + " " + cur2] = time
    if time < 0:
        file.write("weird" + "\n")
    if time == 0:
        # file.write("Base case" + "\n")
        return total
    if len(on) == len(dests):
        # file.write("Terminal case" + "\n")
        return total + per * time
    else:
        best = total + per * time
        if not cur in on and not cur2 in on and cur != cur2:
            on[cur] = True
            on[cur2] = True
            best = max(best, max_flow_helper_2(valves, dests, flows, time - 1, cur, cur2, on, per + flows[cur] + flows[cur2], total + per, seen_states, file))
            del on[cur]
            del on[cur2]
        if not cur in on:
            on[cur] = True
            for candidate in dests[cur2]:
                key_rep = ""
                for valve in valves:
                    if valve in on:
                        key_rep = key_rep + "1"
                    else:
                        key_rep = key_rep + "0"
                next_state = key_rep + " " + cur + " " + candidate
                if not next_state in seen_states or seen_states[next_state] < time - 1:
                    best = max(best, max_flow_helper_2(valves, dests, flows, time - 1, cur, candidate, on, per + flows[cur], total + per, seen_states, file))
            del on[cur]
        if not cur2 in on:
            on[cur2] = True
            for candidate in dests[cur]:
                key_rep = ""
                for valve in valves:
                    if valve in on:
                        key_rep = key_rep + "1"
                    else:
                        key_rep = key_rep + "0"
                next_state = key_rep + " " + candidate + " " + cur2
                if not next_state in seen_states or seen_states[next_state] < time - 1:
                    best = max(best, max_flow_helper_2(valves, dests, flows, time - 1, candidate, cur2, on, per + flows[cur2], total + per, seen_states, file))
            del on[cur2]
        for candidate1 in dests[cur]:
            for candidate2 in dests[cur2]:
                key_rep = ""
                for valve in valves:
                    if valve in on:
                        key_rep = key_rep + "1"
                    else:
                        key_rep = key_rep + "0"
                next_state = key_rep + " " + candidate1 + " " + candidate2
                if not next_state in seen_states or seen_states[next_state] < time - 1:
                    best = max(best, max_flow_helper_2(valves, dests, flows, time - 1, candidate1, candidate2, on, per, total + per, seen_states, file))
        # file.write("Returning best: " + str(best) + " " + str(time) + " " + str(cur) + " " + str(cur2) + " " + ",".join(on.keys()) + " " + str(per) + " " + str(total) + "\n")
        return best

def p1():
    with open('y.txt') as f:
        lines = f.readlines()
        flows = {}
        dests = {}
        for line in lines:
            split_line = line.split()
            valve_name = split_line[1]
            flow = split_line[4].split("=")[1][:-1]
            for ind in range(len(split_line)):
                if(split_line[ind] == "to"):
                    break
            nexts = [x.strip() for x in " ".join(split_line[ind + 2:]).split(",")]
            dests[valve_name] = nexts
            flows[valve_name] = int(flow)
        ans = max_flow(dests, flows, 30, "AA")
        print(ans, flush=True)

def p2():
    with open('y.txt') as f:
        lines = f.readlines()
        flows = {}
        dests = {}
        valves = []
        for line in lines:
            split_line = line.split()
            valve_name = split_line[1]
            flow = split_line[4].split("=")[1][:-1]
            for ind in range(len(split_line)):
                if(split_line[ind] == "to"):
                    break
            nexts = [x.strip() for x in " ".join(split_line[ind + 2:]).split(",")]
            dests[valve_name] = nexts
            flows[valve_name] = int(flow)
            valves.append(valve_name)
        ans = max_flow_double(valves, dests, flows, 26, "AA")
        print(ans, flush=True)

if __name__ == "__main__":
    p2()