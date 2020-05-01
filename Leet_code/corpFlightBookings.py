class Solution:
    def corpFlightBookings(self, bookings, n):
        output = [0]*n
        for x in bookings:
            for i in range(x[0],x[1]+1):
                print(i)
                print(output[0])
                output[i-1]=output[i-1]+x[2]

        return output

class Solution2:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0]*n
        for i in range(1,n+1):
            for x in bookings:
                if x[0]<= i <= x[1]:
                    output[i-1] +=x[2]

        return output


def main():
    obj = Solution()
    A = [[1,2,10],[2,3,20],[2,5,25]]
    print(obj.corpFlightBookings(A, 5))

main()