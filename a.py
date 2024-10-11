from uxsim import *
import tqdm

# シミュレーション本体の定義
# 単位は全て秒とメートル
W = World(
    name="",    # シナリオ名
    deltan=5,   # 車両集計単位
    tmax=1200,  # シミュレーション時間
    print_mode=1, save_mode=1, show_mode=0,    # オプション
    random_seed=0    # ランダムシード
)

# シナリオ定義
## ノードの作成
W.addNode(name="orig1", x=0, y=0)
W.addNode("orig2", 0, 2)
W.addNode("merge", 1, 1)
W.addNode("dest", 2, 1)
## ノード間のリンクの作成
W.addLink(name="link1", start_node="orig1", end_node="merge",
          length=1000, free_flow_speed=20, number_of_lanes=1)
W.addLink("link2", "orig2", "merge", length=1000, free_flow_speed=30, number_of_lanes=1)
W.addLink("link3", "merge", "dest", length=1000, free_flow_speed=30, number_of_lanes=1)
## ノード間のOD交通需要の作成
W.adddemand(orig="orig1", dest="dest", t_start=0, t_end=1000, flow=12)

# シミュレーション実行
W.exec_simulation()

# 結果表示
W.analyzer.print_simple_stats()

# ネットワーク交通状態のスナップショット可視化
for i in tqdm.tqdm(range(0,1200,1)):
    W.analyzer.network(i, detailed=1, network_font_size=12)

