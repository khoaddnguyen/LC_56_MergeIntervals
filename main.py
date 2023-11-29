def merge(self, intervals: List[List[int]]) -> List[List[int]]:

    # sorting O(nlogn): sorting a list of pairs by the start value
    intervals.sort(key = lambda i : i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]  # [-1] is most recently added interval, [1] is the end value

        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)  # [1, 5], [2, 4] ==> [1, 5]
        else:
            output.append([start, end])  # [1, 5], [7, 8] ==> as is
    return output

