# python3

def parallel_processing(n, m, data):
    output = []
    end = [0]*n

    for i in range(m):
        x = min(end)
        thread = end.index(x)
        start = end[thread]
        end[thread] = end[thread] + data[i]
        output.append((thread, start))
        #print(thread)
        #print(start)

    return output

def main():
    count = list(map(int, input().split()))
    n = count[0]
    m = count[1]

    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for i, j in result:
       print(i, j) 

if __name__ == "__main__":
    main()
