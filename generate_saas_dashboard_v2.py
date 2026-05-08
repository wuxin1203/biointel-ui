#!/usr/bin/env python3
"""
BioIntelOS SaaS Dashboard Generator v2
右侧 AI 工作区视觉优化版本 - 科幻风格
"""
from pathlib import Path

OUTPUT = Path(__file__).parent / "biointel-saas-dashboard-v2.html"

# 示例数据集
DATASETS = [
    {
        "id": "GSE100026",
        "tag": "Transcriptomics (Bulk)",
        "title": "Transcriptome characterization of chronic myeloid leukemia by RNA sequencing",
        "species": "Homo sapiens",
        "samples": 63,
        "platform": "Illumina HiSeq 2000"
    },
    {
        "id": "GSE134520",
        "tag": "Spatial Transcriptomics",
        "title": "Liver cancer spatial transcriptome atlas with single-cell resolution",
        "species": "Homo sapiens",
        "samples": 12,
        "platform": "10x Visium"
    },
    {
        "id": "GSE150115",
        "tag": "Single-cell RNA-seq",
        "title": "Intestinal organoid single-cell transcriptome profiling",
        "species": "Mus musculus",
        "samples": 8,
        "platform": "10x Genomics"
    },
    {
        "id": "GSE185224",
        "tag": "Single-cell RNA-seq",
        "title": "Pancreatic ductal adenocarcinoma single-cell atlas",
        "species": "Homo sapiens",
        "samples": 24,
        "platform": "10x Genomics"
    },
    {
        "id": "GSE142025",
        "tag": "Transcriptomics (Bulk)",
        "title": "Colorectal cancer transcriptome profiling across multiple stages",
        "species": "Homo sapiens",
        "samples": 156,
        "platform": "Illumina NovaSeq"
    },
    {
        "id": "GSE167096",
        "tag": "Epigenomics",
        "title": "DNA methylation profiling in breast cancer progression",
        "species": "Homo sapiens",
        "samples": 89,
        "platform": "Illumina 850K"
    },
    {
        "id": "GSE178341",
        "tag": "Single-cell RNA-seq",
        "title": "Immune cell landscape in hepatocellular carcinoma",
        "species": "Homo sapiens",
        "samples": 18,
        "platform": "10x Genomics"
    },
    {
        "id": "GSE191045",
        "tag": "Proteomics",
        "title": "Proteomic profiling of lung adenocarcinoma tissue samples",
        "species": "Homo sapiens",
        "samples": 42,
        "platform": "LC-MS/MS"
    },
    {
        "id": "GSE203567",
        "tag": "Single-cell RNA-seq",
        "title": "Cardiac fibroblast heterogeneity in heart failure",
        "species": "Mus musculus",
        "samples": 16,
        "platform": "10x Genomics"
    }
]

RECOMMENDATIONS = [
    {"id": "GSE134520", "name": "Liver cancer spatial transcriptome atlas"},
    {"id": "GSE150115", "name": "Intestinal organoid scRNA-seq"},
    {"id": "GSE185224", "name": "Pancreatic ductal adenocarcinoma scRNA-seq"}
]

RECENT = [
    {"id": "GSE100026", "name": "Colorectal cancer single-cell...", "time": "今天"},
    {"id": "GSE142025", "name": "Breast cancer transcriptome...", "time": "昨天"},
    {"id": "GSE167096", "name": "DNA methylation profiling...", "time": "3天前"}
]

def generate_dataset_card(ds):
    return f'''      <div class="dataset-card">
        <div class="card-header">
          <div class="dataset-id">{ds["id"]}</div>
          <div class="dataset-tag">{ds["tag"]}</div>
        </div>
        <div class="dataset-title">{ds["title"]}</div>
        <div class="dataset-meta">
          <div class="meta-item"><strong>物种:</strong> {ds["species"]}</div>
          <div class="meta-item"><strong>样本量:</strong> {ds["samples"]}</div>
          <div class="meta-item"><strong>平台:</strong> {ds["platform"]}</div>
        </div>
        <div class="card-footer">
          <button class="add-btn">+ 添加到工作台</button>
          <a href="#" class="detail-link">查看详情 →</a>
        </div>
      </div>'''

def generate_html():
    dataset_cards = "\n\n".join(generate_dataset_card(ds) for ds in DATASETS)

    recommend_items = "\n".join(
        f'''      <div class="recommend-item">
        <div class="recommend-id">{r["id"]}</div>
        <div class="recommend-name">{r["name"]}</div>
      </div>''' for r in RECOMMENDATIONS
    )

    recent_items = "\n".join(
        f'''      <div class="recommend-item">
        <div class="recommend-id">{r["id"]}</div>
        <div class="recommend-name">{r["name"]}</div>
        <div class="recommend-time">{r["time"]}</div>
      </div>''' for r in RECENT
    )

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>BioIntelOS — AI Native Bioinformatics Platform</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB',
    'Microsoft YaHei',Roboto,Helvetica,Arial,sans-serif;
  background:#F8FAF8;color:#1F2937;line-height:1.5;
}}

/* ── Header ── */
.header{{
  height:72px;background:#fff;border-bottom:1px solid #E5E7EB;
  display:flex;align-items:center;padding:0 32px;justify-content:space-between;
}}
.logo{{font-size:22px;font-weight:700;color:#1F2937;letter-spacing:-0.5px}}
.logo span{{background:linear-gradient(135deg,#667eea,#764ba2);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.nav{{display:flex;gap:8px;align-items:center}}
.nav-item{{padding:8px 16px;font-size:14px;font-weight:500;color:#6B7280;
  border-radius:8px;cursor:pointer;transition:all .2s}}
.nav-item:hover{{background:#F3F4F6}}
.nav-item.active{{background:#EAF8EF;color:#16C25B}}
.user-area{{display:flex;align-items:center;gap:10px}}
.avatar{{width:36px;height:36px;border-radius:50%;background:#16C25B;
  display:flex;align-items:center;justify-content:center;color:#fff;font-weight:600;font-size:14px}}
.username{{font-size:14px;font-weight:500;color:#1F2937}}

/* ── Main Layout ── */
.main{{display:flex;height:calc(100vh - 72px);overflow:hidden}}

/* ── Left Sidebar ── */
.sidebar{{width:260px;background:#fff;border-right:1px solid #E5E7EB;
  padding:24px 20px;overflow-y:auto}}
.sidebar-header{{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}}
.sidebar-title{{font-size:18px;font-weight:600;color:#1F2937}}
.clear-btn{{font-size:13px;color:#16C25B;cursor:pointer}}
.filter-section{{margin-bottom:24px}}
.filter-label{{font-size:14px;font-weight:600;color:#1F2937;margin-bottom:12px;display:block}}
.filter-item{{display:flex;align-items:center;justify-content:space-between;
  padding:8px 0;cursor:pointer;transition:all .2s}}
.filter-item:hover{{background:#F9FAFB;margin:0 -8px;padding:8px}}
.filter-item input[type="checkbox"]{{width:16px;height:16px;margin-right:8px;
  accent-color:#16C25B;cursor:pointer}}
.filter-item label{{flex:1;font-size:13px;color:#374151;cursor:pointer}}
.filter-count{{font-size:12px;color:#9CA3AF}}
.search-input{{width:100%;padding:8px 12px;border:1px solid #E5E7EB;border-radius:8px;
  font-size:13px;margin-bottom:8px}}

/* ── Center Area ── */
.center{{flex:1;padding:24px;overflow-y:auto}}
.search-bar{{background:#fff;border-radius:12px;padding:16px;margin-bottom:20px;
  box-shadow:0 1px 3px rgba(0,0,0,0.05)}}
.search-input-main{{display:flex;gap:12px;margin-bottom:12px}}
.search-input-main input{{flex:1;height:52px;border:1px solid #E5E7EB;border-radius:12px;
  padding:0 20px 0 48px;font-size:14px;background:url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="%236B7280" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>') no-repeat 16px center}}
.search-btn{{height:52px;padding:0 24px;background:#16C25B;color:#fff;border:none;
  border-radius:12px;font-weight:600;cursor:pointer;transition:all .2s}}
.search-btn:hover{{background:#14b352}}
.ai-btn{{height:52px;padding:0 24px;background:#fff;color:#16C25B;border:1px solid #16C25B;
  border-radius:12px;font-weight:600;cursor:pointer;display:flex;align-items:center;gap:6px}}
.chips{{display:flex;gap:8px;flex-wrap:wrap}}
.chip{{padding:6px 12px;background:#EAF8EF;color:#16C25B;border-radius:16px;
  font-size:12px;font-weight:500}}

.dataset-header{{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}}
.dataset-count{{font-size:14px;color:#6B7280}}
.dataset-controls{{display:flex;gap:12px;align-items:center}}
.sort-dropdown{{padding:8px 12px;border:1px solid #E5E7EB;border-radius:8px;
  font-size:13px;background:#fff;cursor:pointer}}

/* ── Dataset Cards ── */
.dataset-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.dataset-card{{background:#fff;border-radius:16px;padding:20px;
  box-shadow:0 1px 3px rgba(0,0,0,0.05);border:1px solid #E7EFE7;
  transition:all .2s;cursor:pointer;height:240px;display:flex;flex-direction:column}}
.dataset-card:hover{{box-shadow:0 4px 12px rgba(0,0,0,0.08);transform:translateY(-2px)}}
.card-header{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px}}
.dataset-id{{font-size:18px;font-weight:700;color:#16C25B}}
.dataset-tag{{padding:4px 10px;background:#EAF8EF;color:#16C25B;border-radius:6px;
  font-size:11px;font-weight:600;text-transform:uppercase}}
.dataset-title{{font-size:15px;font-weight:600;color:#1F2937;margin-bottom:12px;
  line-height:1.4;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;
  overflow:hidden;flex:1}}
.dataset-meta{{display:flex;flex-direction:column;gap:6px;margin-bottom:16px}}
.meta-item{{font-size:13px;color:#6B7280}}
.meta-item strong{{color:#374151;font-weight:500}}
.card-footer{{display:flex;justify-content:space-between;align-items:center;margin-top:auto}}
.add-btn{{padding:8px 16px;background:#EAF8EF;color:#16C25B;border:1px solid #16C25B;
  border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;transition:all .2s}}
.add-btn:hover{{background:#16C25B;color:#fff}}
.detail-link{{font-size:13px;color:#16C25B;font-weight:600;text-decoration:none}}

/* ── Right Sidebar - AI 智能工作区（浅绿科幻风格）── */
.right-sidebar{{
  width:340px;
  background:linear-gradient(180deg, #E8F5EE 0%, #E0F0E8 100%);
  border-left:1px solid rgba(22,194,91,0.3);
  padding:24px 20px;
  overflow-y:auto;
  position:relative;
}}
.right-sidebar::before{{
  content:'';
  position:absolute;
  top:0;left:0;right:0;bottom:0;
  background:radial-gradient(circle at 50% 0%, rgba(22,194,91,0.12) 0%, transparent 60%);
  pointer-events:none;
}}

.ai-card{{
  background:rgba(255,255,255,0.85);
  backdrop-filter:blur(10px);
  border:1px solid rgba(22,194,91,0.25);
  border-radius:16px;
  padding:20px;
  margin-bottom:24px;
  box-shadow:0 4px 20px rgba(22,194,91,0.15), inset 0 1px 0 rgba(255,255,255,0.8);
  position:relative;
}}
.ai-card::after{{
  content:'';
  position:absolute;
  top:-1px;left:20px;right:20px;
  height:1px;
  background:linear-gradient(90deg, transparent, rgba(22,194,91,0.5), transparent);
}}

.ai-header{{
  display:flex;
  justify-content:space-between;
  align-items:center;
  margin-bottom:16px;
}}
.ai-title{{
  font-size:16px;
  font-weight:600;
  color:#16C25B;
  text-shadow:0 0 10px rgba(22,194,91,0.5);
  letter-spacing:0.5px;
}}

.ai-avatar{{
  width:48px;height:48px;
  border-radius:50%;
  background:linear-gradient(135deg, #16C25B 0%, #0EA34D 100%);
  display:flex;align-items:center;justify-content:center;
  margin-bottom:12px;
  box-shadow:0 0 20px rgba(22,194,91,0.6), 0 0 40px rgba(22,194,91,0.3);
  animation:pulse-glow 3s ease-in-out infinite;
}}
@keyframes pulse-glow{{
  0%, 100%{{box-shadow:0 0 20px rgba(22,194,91,0.6), 0 0 40px rgba(22,194,91,0.3)}}
  50%{{box-shadow:0 0 30px rgba(22,194,91,0.8), 0 0 60px rgba(22,194,91,0.4)}}
}}

.ai-welcome{{
  font-size:13px;
  color:rgba(0,0,0,0.7);
  line-height:1.6;
  margin-bottom:16px;
}}

.ai-suggestions{{
  display:flex;
  flex-direction:column;
  gap:8px;
  margin-bottom:16px;
}}
.ai-suggestion{{
  padding:10px 14px;
  background:rgba(22,194,91,0.08);
  border:1px solid rgba(22,194,91,0.25);
  border-radius:8px;
  font-size:12px;
  color:rgba(0,0,0,0.75);
  cursor:pointer;
  transition:all .3s ease;
  position:relative;
  overflow:hidden;
}}
.ai-suggestion::before{{
  content:'';
  position:absolute;
  top:0;left:-100%;
  width:100%;height:100%;
  background:linear-gradient(90deg, transparent, rgba(22,194,91,0.2), transparent);
  transition:left .5s;
}}
.ai-suggestion:hover{{
  border-color:#16C25B;
  color:#16C25B;
  background:rgba(22,194,91,0.15);
  box-shadow:0 0 15px rgba(22,194,91,0.3);
  transform:translateX(4px);
}}
.ai-suggestion:hover::before{{left:100%}}

.ai-input-wrap{{position:relative}}
.ai-input{{
  width:100%;
  padding:12px 44px 12px 14px;
  background:rgba(255,255,255,0.7);
  border:1px solid rgba(22,194,91,0.3);
  border-radius:8px;
  font-size:13px;
  color:rgba(0,0,0,0.85);
  transition:all .3s;
}}
.ai-input:focus{{
  outline:none;
  border-color:#16C25B;
  box-shadow:0 0 15px rgba(22,194,91,0.4);
  background:rgba(255,255,255,0.9);
}}
.ai-input::placeholder{{color:rgba(0,0,0,0.4)}}

.ai-send{{
  position:absolute;right:8px;top:50%;transform:translateY(-50%);
  width:32px;height:32px;
  background:linear-gradient(135deg, #16C25B 0%, #0EA34D 100%);
  border-radius:50%;border:none;
  color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 0 15px rgba(22,194,91,0.5);
  transition:all .3s;
}}
.ai-send:hover{{
  box-shadow:0 0 25px rgba(22,194,91,0.8);
  transform:translateY(-50%) scale(1.1);
}}

.recommend-section{{
  margin-bottom:24px;
  position:relative;
}}
.recommend-title{{
  font-size:15px;
  font-weight:600;
  color:#16C25B;
  margin-bottom:12px;
  text-shadow:0 0 8px rgba(22,194,91,0.3);
}}

.recommend-item{{
  background:rgba(255,255,255,0.5);
  border:1px solid rgba(22,194,91,0.2);
  border-radius:8px;
  padding:12px;
  margin-bottom:8px;
  cursor:pointer;
  transition:all .3s ease;
  position:relative;
}}
.recommend-item::before{{
  content:'';
  position:absolute;
  left:0;top:0;bottom:0;
  width:2px;
  background:#16C25B;
  opacity:0;
  transition:opacity .3s;
}}
.recommend-item:hover{{
  background:rgba(22,194,91,0.08);
  border-color:rgba(22,194,91,0.4);
  transform:translateX(4px);
  box-shadow:0 0 15px rgba(22,194,91,0.2);
}}
.recommend-item:hover::before{{opacity:1}}

.recommend-id{{
  font-size:12px;
  font-weight:600;
  color:#16C25B;
  margin-bottom:4px;
  text-shadow:0 0 5px rgba(22,194,91,0.3);
}}
.recommend-name{{
  font-size:12px;
  color:rgba(0,0,0,0.7);
  line-height:1.4;
}}
.recommend-time{{
  font-size:11px;
  color:rgba(0,0,0,0.5);
  margin-top:4px;
}}
</style>
</head>
<body>

<!-- Header -->
<div class="header">
  <div class="logo">BioIntel<span>O</span>S</div>
  <div class="nav">
    <div class="nav-item">智能助手</div>
    <div class="nav-item active">数据集</div>
    <div class="nav-item">个人设置</div>
  </div>
  <div class="user-area">
    <div class="avatar">JX</div>
    <div class="username">jyxiao</div>
  </div>
</div>

<!-- Main Layout -->
<div class="main">

  <!-- Left Sidebar -->
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">筛选条件</div>
      <div class="clear-btn">清空</div>
    </div>

    <div class="filter-section">
      <span class="filter-label">数据集类型</span>
      <div class="filter-item">
        <input type="checkbox" id="geo" checked>
        <label for="geo">GEO</label>
        <span class="filter-count">8,234</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="tcga">
        <label for="tcga">TCGA</label>
        <span class="filter-count">1,542</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="cbio">
        <label for="cbio">cBioPortal</label>
        <span class="filter-count">892</span>
      </div>
    </div>

    <div class="filter-section">
      <span class="filter-label">物种（Organism）</span>
      <input type="text" class="search-input" placeholder="搜索物种...">
      <div class="filter-item">
        <input type="checkbox" id="human" checked>
        <label for="human">Homo sapiens</label>
        <span class="filter-count">6,421</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="mouse">
        <label for="mouse">Mus musculus</label>
        <span class="filter-count">2,103</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="rat">
        <label for="rat">Rattus norvegicus</label>
        <span class="filter-count">456</span>
      </div>
    </div>

    <div class="filter-section">
      <span class="filter-label">数据类型</span>
      <div class="filter-item">
        <input type="checkbox" id="trans" checked>
        <label for="trans">Transcriptomics</label>
        <span class="filter-count">5,234</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="epi">
        <label for="epi">Epigenomics</label>
        <span class="filter-count">1,892</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="prot">
        <label for="prot">Proteomics</label>
        <span class="filter-count">743</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="meta">
        <label for="meta">Metagenomics</label>
        <span class="filter-count">521</span>
      </div>
    </div>

    <div class="filter-section">
      <span class="filter-label">研究领域</span>
      <div class="filter-item">
        <input type="checkbox" id="cancer" checked>
        <label for="cancer">Cancer</label>
        <span class="filter-count">3,421</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="immuno">
        <label for="immuno">Immunology</label>
        <span class="filter-count">1,234</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="neuro">
        <label for="neuro">Neurology</label>
        <span class="filter-count">892</span>
      </div>
      <div class="filter-item">
        <input type="checkbox" id="cardio">
        <label for="cardio">Cardiovascular</label>
        <span class="filter-count">567</span>
      </div>
    </div>
  </div>

  <!-- Center Area -->
  <div class="center">
    <div class="search-bar">
      <div class="search-input-main">
        <input type="text" placeholder="输入关键词搜索数据集，如：liver cancer, single-cell RNA-seq...">
        <button class="search-btn">搜索</button>
        <button class="ai-btn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
          </svg>
          AI 检索
        </button>
      </div>
      <div class="chips">
        <div class="chip">GSE100026</div>
        <div class="chip">RNA-seq</div>
        <div class="chip">Homo sapiens</div>
        <div class="chip">liver cancer</div>
      </div>
    </div>

    <div class="dataset-header">
      <div class="dataset-count">显示 {len(DATASETS)} / 15,544 个数据集</div>
      <div class="dataset-controls">
        <select class="sort-dropdown">
          <option>相关性</option>
          <option>最新发布</option>
          <option>样本量</option>
        </select>
      </div>
    </div>

    <div class="dataset-grid">
{dataset_cards}
    </div>
  </div>

  <!-- Right Sidebar -->
  <div class="right-sidebar">
    <div class="ai-card">
      <div class="ai-header">
        <div class="ai-title">AI 助手</div>
      </div>
      <div class="ai-avatar">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2">
          <path d="M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V7h1a7 7 0 0 1 7 7h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-1H2a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h1a7 7 0 0 1 7-7h1V5.73c-.6-.34-1-.99-1-1.73a2 2 0 0 1 2-2z"/>
          <circle cx="9" cy="14" r="1"/><circle cx="15" cy="14" r="1"/>
        </svg>
      </div>
      <div class="ai-welcome">Hi! 我是 BioIntelOS AI 助手<br>我可以帮你检索数据、解读结果、推荐相关数据集</div>
      <div class="ai-suggestions">
        <div class="ai-suggestion">寻找肝癌的单细胞转录组数据集</div>
        <div class="ai-suggestion">推荐乳腺癌的表达谱数据集</div>
        <div class="ai-suggestion">比较不同平台的肝癌数据差异</div>
      </div>
      <div class="ai-input-wrap">
        <input type="text" class="ai-input" placeholder="输入你的问题...">
        <button class="ai-send">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
          </svg>
        </button>
      </div>
    </div>

    <div class="recommend-section">
      <div class="recommend-title">你可能想找</div>
{recommend_items}
    </div>

    <div class="recommend-section">
      <div class="recommend-title">最近常用</div>
{recent_items}
    </div>
  </div>

</div>

</body>
</html>'''
    return html

def main():
    html = generate_html()
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"SaaS Dashboard 已生成: {OUTPUT}")
    print(f"数据集数量: {len(DATASETS)}")

if __name__ == "__main__":
    main()
