# 動作説明
1. start_points = np.random.rand(n, 2)  
   ボロノイ図を作るための点をランダムに設定します。
2. vor = Voronoi(start_points)  
   ボロノイ図のそれぞれの輪郭の点の座標と線の繋がりを生成します。
3. polygons = get_effective_polygons(vor.regions)  
   閉じられた輪郭の図形を抽出します。
4. touching_polygons = get_touching_polygons(polygons)  
   隣接する閉じられた図形の番号を取得します。
5. colors = set_colors(polygons, touching_polygons)  
   全てが隣り合わない色の組み合わせを計算します。
6. paint_colors(polygons, colors)  
    色を塗ります。

# アルゴリズム
colors:polygonsに対応する同じ場所の色  
choices:polygonsに対応する隣接する色の数  
アルゴリズムの説明のため、  
color:現在のマスの色の候補  
choice:現在のマスに隣接する色の数  
とする。  
1. もし、choiceの候補の色以降に可能な色がない、または候補の色が最後の色、または以降マス(未定のマス)に全ての色に隣接するマスがあるなら
   1. colorが決まっていたなら、未定にする。
   2. 前のマスに戻る。
2. colorを次の候補にする。
3. 次のマスへ進む。
4. もし最後が終わったら、ループを抜ける。
1~4をループする。
