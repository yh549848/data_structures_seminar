# 赤黒木 (Red-Black Trees)

## What's this

> **赤黒木**（あかくろぎ）は、[コンピュータ科学](https://ja.wikipedia.org/wiki/コンピュータ科学)の[データ構造](https://ja.wikipedia.org/wiki/データ構造)である[平衡二分木](https://ja.wikipedia.org/wiki/平衡2分探索木)の一種で、主に[連想配列](https://ja.wikipedia.org/wiki/連想配列)の実装に用いられている。**2色木**、**レッド・ブラック・ツリー**ともいう。
>
> 出典: フリー百科事典『ウィキペディア（Wikipedia）』

- 二分探索木（Binary search tree）の一種
- insert(), delete(), search()のいづれも最善:  O(log n)
- 連想配列の実装へ広く採用されている（一方，実装が複雑）
- 或る赤黒木には，対応する 2-4木（2-4 trees）が存在する



##  2-4 Trees

赤黒木の説明の前に2-4木を説明する．

- B=2のB木（B-tree）である（テキスト14章）

- 2-4木は以下の性質を持つ

  - (degree) すべての内部ノードは2, 3 or 4の子ノードを持つ
  - (height) すべての葉の深さは等しい
  
- 雑記: 実装が複雑

  


##Red-Black trees

- 高さが logarithmic な二分探索木（SSetインターフェースの実装のひとつ）
- すべてのリーフの深さは等しい


- 赤黒木は以下の性質を持つ．
  
  - (black-height) ルートからリーフへのパスには**同数の黒のノード**が含まれる
  - (no-red-edge) **赤のノードは隣接しない**
- 色を付けることの何がうれしいのか？
  
  
  - 2-4木を二分探索木として取り扱うことができる
  
    - たかだか1ビットの情報によって実装で考慮すべきことが
- 雑記: 実装が複雑，だが，2-4木よりは容易（らしい）
- 参考動画

  - https://youtu.be/PhY56LpCtP4
  - https://youtu.be/axa2g5oOzCE

### Left-leaning Red-Black trees

- 左傾赤黒木は以下の性質（制約）を持つ
- (left-leaning) 或るノードの左の子ノードが黒ノードならば，右の子ノードも黒ノードである
    - \* つまり，赤ノードが左の子ノードへ偏り，3-nodesの2-4木のノードに対して赤黒木の形が一意に定まるようになる
    - 上記のおかげで実装で考慮するべきパターンが減る



# ヒープ（Heaps）

## What's this

> **ヒープ**（[英](https://ja.wikipedia.org/wiki/英語): heap）とは、「子要素は親要素より常に大きいか等しい（または常に小さいか等しい）」という制約を持つ[木構造](https://ja.wikipedia.org/wiki/木構造_(データ構造))の事。
>
> 出典: フリー百科事典『ウィキペディア（Wikipedia）』

- 優先度付きキュー（Priority Queue）インターフェースの実装のひとつ
- ヒープ性を満たしている木構造
- https://medium.com/@yasufumy/data-structure-heap-ecfd0989e5be
- 何がうれしいのか？
  - ソートが速い（heap sort > quick sort）（テキスト11章）
- 雑記: "heap"は，「雑多に積まれた」というニュアンス．ヒープ（メモリ領域）は，必ずしもヒープ（データ構造）ではないらしい．



## Binary Heaps

- 優先度付きキュー（Priority Queue）インターフェースの実装のひとつ
- 二分木データ構造によるヒープの表現
  - 実際には配列が用いられることが多い．
  - 完全二分木
- バイナリヒープは以下の性質を持つ
  - 子ノードの値 >=  親ノード（或いはこの逆の関係）

## Meldable Heaps

- 優先度付きキュー（Priority Queue）インターフェースの実装のひとつ
- mergeできる

## Appendix

![Screen Shot 2019-06-15 at 2.10.58](https://github.com/yh549848/ods/blob/master/09_red_black_trees/images/Screen%20Shot%202019-06-15%20at%202.10.58.png)
