# 1631. 最小体力消耗路径
# 和 778 差不多，感觉还要难一些(怪不得看778题感觉似曾相识)

# 我们将这 mn 个节点放入并查集中，实时维护它们的连通性。
# 由于我们需要找到从左上角到右下角的最短路径，因此我们可以将图中的所有边按照权值从小到大进行排序，并依次加入并查集中。
# 当我们加入一条权值为 x 的边之后，如果左上角和右下角从非连通状态变为连通状态，那么 x 即为答案。

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
