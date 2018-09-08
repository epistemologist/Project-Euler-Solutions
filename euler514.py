def euler514():
    from scipy.spatial import ConvexHull
    import random
    def geoboard(N):
        points = []
        for i in range(N):
            for j in range(N):
                if random.random()<1./(N+1):
                    points.append((i,j))
        try:
            return ConvexHull(points).area
        except:
            return 0
    def average(arr):
        return float(sum(arr))/len(arr)
    return average([geoboard(2) for _ in range(10000)])
print euler514()