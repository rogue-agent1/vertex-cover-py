#!/usr/bin/env python3
"""Minimum vertex cover — 2-approximation for general graphs."""

def vertex_cover_approx(n, edges):
    """2-approximation: greedily pick both endpoints of uncovered edges."""
    cover = set(); covered = set()
    for i, (u, v) in enumerate(edges):
        if i not in covered:
            cover.add(u); cover.add(v)
            for j, (a, b) in enumerate(edges):
                if a in cover or b in cover: covered.add(j)
    return cover

def vertex_cover_exact(n, adj):
    """Exact via complement of max independent set (small graphs only)."""
    adj_mask = [0]*n
    for u in range(n):
        for v in adj[u]: adj_mask[u] |= 1 << v
    best = n
    for mask in range(1 << n):
        # Check if mask is a vertex cover
        is_cover = True
        for u in range(n):
            if not (mask & (1 << u)):
                if adj_mask[u] & ~mask: is_cover = False; break
        if is_cover: best = min(best, bin(mask).count('1'))
    return best

def main():
    adj = [[1,2],[0,2],[0,1,3],[2]]
    print(f"Min vertex cover: {vertex_cover_exact(4, adj)}")

if __name__ == "__main__": main()
