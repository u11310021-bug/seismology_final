import gradio as gr
import matplotlib.pyplot as plt
from obspy.imaging.beachball import beachball
import os

def plot_beachball(strike, dip, rake):
    """
    根據使用者輸入的 Strike, Dip, Rake 產生震源機制球
    """
    try:
        strike = float(strike)
        dip = float(dip)
        rake = float(rake)
    except (ValueError, TypeError):
        return None
    
    focal_mechanism = [strike, dip, rake]
    
    plt.clf()
    plt.close('all')
    
    fig = beachball(focal_mechanism, size=200, linewidth=2, facecolor='dodgerblue')
    return fig

custom_css = """
body, .gradio-container {
    background-color: #1a1a24 !important;
    color: #e0e0e0 !important;
}
"""

theme = gr.themes.Monochrome(
    primary_hue="indigo",
    neutral_hue="slate"
).set(
    body_background_fill="#1a1a24",
    body_background_fill_dark="#1a1a24",
    block_background_fill="#252535",
    block_background_fill_dark="#252535",
    block_label_text_color="white",
    body_text_color="white"
)

with gr.Blocks(theme=theme, css=custom_css) as demo:
    gr.Markdown("# 🌍 地震震源機制球與課本內容分享")
    
    with gr.Tabs():
        # 分頁 1: 作業8分享
        with gr.TabItem("作業8分享"):
            gr.Markdown("## 作業8：繪製震源機制球")
            gr.Markdown(
                "**作業摘要與背景資料：**\n\n"
                "本次作業以 2025 年發生於日本青森的強震為例，探討並視覺化震源機制。以下為該次地震的 USGS 觀測資料："
            )
            
            # USGS Data Presentation
            with gr.Group():
                gr.Markdown("### 🔍 USGS 地震事件資料 (us6000rtdt)")
                gr.Markdown(
                    "- **地震規模 (Magnitude):** M 7.6\n"
                    "- **震央位置 (Location):** Aomori Prefecture, Japan (日本青森縣外海)\n"
                    "- **發生時間 (Time):** 2025-12-08 14:15:09 UTC\n"
                    "- **深度 (Depth):** 40.7 km\n"
                    "- **震源機制 (Moment Tensor NP1):** 走向 (Strike) 184° / 傾角 (Dip) 17° / 滑移角 (Rake) 71°\n"
                    "*[資料來源：USGS Earthquake Hazards Program]*"
                )
                
            gr.Markdown("### 作業流程說明與產出")
            with gr.Column():
                gr.Markdown("#### HW8-1：資料獲取與背景分析")
                gr.Image("HW8-1.png", label="HW8-1", show_label=True)
                gr.Markdown(
                    "**詳細說明：**\n"
                    "這張圖擷取了本次作業所探討的 **2025 年日本青森縣外海 M7.6 地震** 的基本背景資料。\n"
                    "- **震央與構造環境**：地震發生在「聚合型板塊邊界」，也就是太平洋板塊向日本海溝隱沒的區域。\n"
                    "- **地震機制**：這是一起典型的「隱沒帶逆衝型地震」(Megathrust earthquake)。其成因是海洋板塊隱沒時與大陸板塊界面鎖定，應力持續累積後引發的突然破裂。\n"
                    "- **特徵**：這類地震通常伴隨大規模的破裂面、長週期的地震波，且因為發生在海底，往往具有強烈的海嘯潛勢。"
                )
                
                gr.Markdown("#### HW8-2：斷層參數定義與走向傾角滑移角分析")
                gr.Image("HW8-2.png", label="HW8-2", show_label=True)
                gr.Markdown(
                    "**詳細說明：**\n"
                    "圖中詳細列出了本次地震的震源機制參數 (Strike, Dip, Rake) 及其物理意義：\n"
                    "- **Strike (走向) = 184°**：這代表斷層面的延伸方向幾乎是南北向。\n"
                    "- **Dip (傾角) = 17°**：顯示斷層面向西呈現「極平緩」的傾斜，這與隱沒帶板塊界面的淺層傾角特徵非常吻合。\n"
                    "- **Rake (滑移角) = 71°**：根據右側的對照表 (90°為純逆衝)，71° 代表這是一個「逆衝偏右移走滑」的錯動機制。"
                )
                
                gr.Markdown("#### HW8-3：震源機制球手繪結果")
                gr.Image("HW8-3.png", label="HW8-3", show_label=True)
                gr.Markdown(
                    "**詳細說明：**\n"
                    "這是作業的最終產出——一張手繪的震源機制球 (Beachball) 草圖，對應參數為 `184/17/71`。\n"
                    "圖中透過兩條節面 (Nodal planes) 將圓分為四個區域，中間劃上斜線的區域代表 P波初動為向上的「壓縮區 (Compression)」，而空白處則為「伸張區 (Dilatation)」。這顆海灘球的外觀呈現中間被大面積壓縮區覆蓋的「貓眼」形狀，是典型低傾角逆衝斷層 (Thrust fault) 的特徵圖形。"
                )

            gr.Markdown("您可以透過下方檢視或下載原始作業 PDF 檔案：")
            gr.File(value="作業8-繪製震源機制球.pdf", label="作業8-繪製震源機制球.pdf")
            
        # 分頁 2: 4.1 & 4.2 課本內容
        with gr.TabItem("4.1 & 4.2 課本內容"):
            gr.Markdown("## 課本內容統整與圖解說明")
            
            with gr.Group():
                gr.Markdown("### 📖 4.1 簡介 (Introduction)")
                gr.Markdown(
                    "主要介紹地震與斷層活動的基本概念。地震起因於地殼內部的應力累積，當應力超過岩石強度時，便會沿著薄弱的斷層面發生錯動，釋放累積的能量進而產生地震波。"
                )
                with gr.Column():
                    gr.Image("fig4.1-3.png", label="圖 4.1-3：彈性回跳理論與應力累積概念", show_label=True)
                    gr.Markdown(
                        "**詳細說明：**\n"
                        "這張圖展示了地震學中經典的「彈性回跳理論 (Elastic Rebound Theory)」：\n"
                        "- **(a)**：斷層兩側原本有筆直的特徵（如柵欄），此時斷層處於鎖定 (Locked) 狀態。\n"
                        "- **(b)**：隨著板塊運動，斷層兩側的物質發生相對位移，使得地殼產生彈性變形與應力累積，柵欄因此跟著彎曲。\n"
                        "- **(c)**：當累積的應力超過斷層的摩擦力與岩石強度時，斷層瞬間破裂並發生滑移，釋放累積的能量產生地震，兩側的柵欄也被永久錯開。"
                    )
            
            with gr.Group():
                gr.Markdown("### 📖 4.2 震源機制 (Focal Mechanisms)")
                gr.Markdown(
                    "震源機制球是用來表示地震斷層錯動方式的圖形化工具。我們主要透過以下三個角度參數來描述斷層的幾何與錯動特徵："
                )
                with gr.Column():
                    gr.Image("fig4.2-2.png", label="圖 4.2-2：走向 (Strike) 與斷層幾何示意圖", show_label=True)
                    gr.Markdown(
                        "**詳細說明：**\n"
                        "本圖定義了斷層的 3D 幾何結構：\n"
                        "- 斷層面將地層分為上盤 (Hanging wall) 與下盤 (Foot wall)。\n"
                        "- **走向 (Strike angle, φf)**：斷層面與地表水平面交線的方向，以正北依順時針方向測量。\n"
                        "- **傾角 (Dip angle, δ)**：斷層面深入地下的傾斜角度。\n"
                        "- **滑移角 (Slip angle / Rake, λ)**：上盤相對於下盤滑動的方向向量 (Slip vector, d) 與走向線之間的夾角。"
                    )
                    
                    gr.Image("fig4.2-3.png", label="圖 4.2-3：基本斷層型態分類", show_label=True)
                    gr.Markdown(
                        "**詳細說明：**\n"
                        "這張圖根據滑移角 (λ) 的數值，展示了四種最基本的斷層型態：\n"
                        "- **左移走滑斷層 (Left-lateral strike-slip)**：λ = 0°，斷層兩側平行水平錯動，對側向左移。\n"
                        "- **右移走滑斷層 (Right-lateral strike-slip)**：λ = 180°，對側向右移。\n"
                        "- **正斷層 (Normal dip-slip)**：λ = -90°，上盤沿斷層面向下滑動，通常發生在張裂環境。\n"
                        "- **逆衝斷層 (Reverse dip-slip)**：λ = 90°，上盤沿斷層面向上滑動，通常發生在擠壓環境。"
                    )
                    
                    gr.Image("fig4.2-4.png", label="圖 4.2-4：P波初動與節面 (Nodal planes)", show_label=True)
                    gr.Markdown(
                        "**詳細說明：**\n"
                        "圖中展示了地震波 (P波) 的初動方向如何被用來推斷斷層方向：\n"
                        "- 斷層錯動時，會將周遭的岩體分為四個象限：兩個「壓縮區 (Compression)」(P波初動向上/向外) 與兩個「伸張區 (Dilatation)」(P波初動向下/向內)。\n"
                        "- 分隔這四個象限的兩個正交平面稱為「節面 (Nodal planes)」。其中一個是實際滑動的**斷層面 (Fault plane)**，另一個是**輔助面 (Auxiliary plane)**。單靠地震波形無法分辨哪一個才是真實斷層面，需結合地質背景判斷。"
                    )
                    
                gr.Markdown(
                    "透過上述參數，我們可以將三維的斷層活動投影至二維平面的「海灘球」上。下圖 4.2-15 展示了不同斷層型態（正斷層、逆斷層、平移斷層）所對應的標準震源機制球圖形。"
                )
                with gr.Column():
                    gr.Image("fig4.2-15.png", label="圖 4.2-15：各類斷層的震源機制球特徵", show_label=True)
                    gr.Markdown(
                        "**詳細說明：**\n"
                        "這是一張非常實用的對照表，展示了一個南北走向 (N-S striking) 的斷層，在不同滑移角 (Rake, λ) 下所對應的海灘球形狀變化：\n"
                        "- **λ = 90° (純逆衝斷層)**：海灘球呈現中間黑色的「貓眼」狀。\n"
                        "- **λ = 180° (純右移平移斷層)**：海灘球呈現黑白相間的「十字/BMW」型態。\n"
                        "- **λ = 270° (或 -90°, 純正斷層)**：海灘球呈現中間白色的形狀（代表中心為伸張區）。\n"
                        "透過這張圖表，我們可以由海灘球的外觀，快速直覺地判斷出地震發生的斷層性質。"
                    )
            
            gr.Markdown("下方為相關講義 PDF 檔案，供詳細閱讀：")
            gr.File(value=["25_4.1 Introduction.pdf", "26_4.2 Focal mechanisms.pdf"], label="4.1 & 4.2 講義檔案")

        # 分頁 3: 震源機制球產生器
        with gr.TabItem("震源機制球產生器"):
            gr.Markdown("## 互動式震源機制球產生器")
            gr.Markdown("請在下方輸入斷層的走向、傾角與滑移角（您可以嘗試輸入 USGS 提供的青森地震參數：Strike 184, Dip 17, Rake 71），系統將自動繪製出對應的震源機制球。")
            
            with gr.Row():
                with gr.Column():
                    strike_input = gr.Number(value=184, label="走向 (Strike, 0~360°)", precision=0)
                    dip_input = gr.Number(value=17, label="傾角 (Dip, 0~90°)", precision=0)
                    rake_input = gr.Number(value=71, label="滑移角 (Rake, -180~180°)", precision=0)
                    submit_btn = gr.Button("產生震源機制球", variant="primary")
                    
                with gr.Column():
                    output_plot = gr.Plot(label="震源機制球圖形")
                    
            submit_btn.click(
                fn=plot_beachball, 
                inputs=[strike_input, dip_input, rake_input], 
                outputs=output_plot
            )

if __name__ == "__main__":
    demo.launch()
