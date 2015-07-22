import bt

if __name__ == "__main__":

    tree = bt.build(
        (1, 2, (3, (4, 5, (6, 7, None)), None))
        )

    print tree
    
    assert tree.exists(7)
    assert not tree.exists(8)

    assert tree.distance(7) == 4
    assert tree.path(7) == [7, 6, 4, 3, 1]
    
    print tree.levels()