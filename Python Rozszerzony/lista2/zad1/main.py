
# result of elections in dictionary {party_name: votes};number of seats
def elections(results, seats):
    total_votes = sum(results.values())
    # sort results so in case of same amount of votes max will find the biggest party (Polish solution)
    sorted_results = {key: value for key, value in sorted(results.items(), key=lambda item: item[1], reverse=True)}
    # prepare data for processing (key: [votes, seats]), apply 5% threshold
    new_results = {key: [value, 0] for key, value in sorted_results.items() if (value/total_votes >= 0.05)}
    for i in range(1, seats + 1):
        # get key with most voters
        mx_key = max(new_results, key=lambda party: new_results[party][0])
        # update elections
        new_results[mx_key][0] //= i
        new_results[mx_key][1] += 1
    return {key: value[1] for key, value in new_results.items()}

if __name__ == '__main__':
    print(elections({"PO": 70122, "PiS": 60013, "Lewica": 100456, "3D": 12329, "Konfederacja": 5}, 12))
