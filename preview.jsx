import React, { useEffect, useState, useRef } from "react";
import * as XLSX from "xlsx";
import * as d3 from "d3";
import * as echarts from "echarts";

// CirclePacking 组件
function CirclePacking({ data }) {
  const ref = useRef();

  useEffect(() => {
    if (!data.length) return;

    const speciesCounts = d3.rollup(data, (v) => v.length, (d) => d.species);
    const root = d3.hierarchy({
      children: Array.from(speciesCounts, ([name, value]) => ({ name, value })),
    }).sum((d) => d.value);

    const pack = d3.pack().size([300, 300]).padding(5);
    const nodes = pack(root).descendants();

    const svg = d3.select(ref.current);
    svg.selectAll("*").remove();
    const g = svg.append("g");

    g.selectAll("circle")
      .data(nodes.filter((d) => !d.children))
      .enter()
      .append("circle")
      .attr("cx", (d) => d.x)
      .attr("cy", (d) => d.y)
      .attr("r", (d) => d.r)
      .attr("fill", "#22c55e")
      .attr("opacity", 0.6);

    g.selectAll("text")
      .data(nodes.filter((d) => !d.children))
      .enter()
      .append("text")
      .attr("x", (d) => d.x)
      .attr("y", (d) => d.y)
      .attr("text-anchor", "middle")
      .attr("dy", ".3em")
      .text((d) => d.data.name)
      .style("font-size", "10px");
  }, [data]);

  return <svg ref={ref} width={300} height={300} />;
}

// 主页面组件
export default function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // 读取 Excel 文件
    fetch("/mnt/data/datset_demo100.xlsx") // 请确保路径正确
      .then((res) => res.arrayBuffer())
      .then((buffer) => {
        const workbook = XLSX.read(buffer);
        const sheet = workbook.Sheets[workbook.SheetNames[0]];
        const json = XLSX.utils.sheet_to_json(sheet);
        const clean = json.map((d) => ({
          species: d.物种, 
          tissue: extractTissue(d.组织), 
          disease: extractDisease(d.疾病), 
          omics: normalizeOmics(d.数据类型（组学）), 
          sample_num: d.数据样本数, 
          dataset: d.数据类型（组学）
        }));
        setData(clean);
      });
  }, []);

  useEffect(() => {
    if (!data.length) return;

    const nodesSet = new Set();
    const links = [];

    data.forEach((d) => {
      const s = d.species;
      const t = d.tissue;
      const dis = d.disease;

      nodesSet.add(s);
      nodesSet.add(t);
      nodesSet.add(dis);

      links.push({ source: s, target: t, value: 1 });
      links.push({ source: t, target: dis, value: 1 });
    });

    const sankey = echarts.init(document.getElementById("sankey"));
    sankey.setOption({
      series: [
        {
          type: "sankey",
          data: Array.from(nodesSet).map((n) => ({ name: n })),
          links,
          lineStyle: { color: "source", curveness: 0.5 },
        },
      ],
    });
  }, [data]);

  return (
    <div className="bg-gray-50 min-h-screen p-8">
      <div className="text-3xl font-bold mb-2 text-green-600">BioIntelOS</div>
      <div className="text-gray-500 mb-6">Multi-omics Data Portal</div>

      <div className="grid grid-cols-5 gap-4 mb-6">
        <StatCard title="Datasets" value={data.length} />
        <StatCard title="Species" value={[...new Set(data.map((d) => d.species))].length} />
        <StatCard title="Tissues" value={[...new Set(data.map((d) => d.tissue))].length} />
        <StatCard title="Diseases" value={[...new Set(data.map((d) => d.disease))].length} />
        <StatCard title="Omics" value={[...new Set(data.map((d) => d.omics))].length} />
      </div>

      <div className="grid grid-cols-3 gap-6">
        <ChartCard title="Species Distribution" desc="Circle Packing view">
          <CirclePacking data={data} />
        </ChartCard>
        <ChartCard title="Meta Summary" desc="Quick overview">
          <div className="text-sm text-gray-600">
            Integrated multi-omics datasets across species, tissues, and diseases.
          </div>
        </ChartCard>
        <div className="col-span-3 bg-white rounded-2xl shadow p-4">
          <div className="font-semibold">Species–Tissue–Disease Sankey</div>
          <div id="sankey" className="h-[400px]" />
        </div>
      </div>
    </div>
  );
}

// Helper functions for extracting and normalizing data

function extractDisease(title) {
  if (!title) return "Unknown";
  if (title.toLowerCase().includes("carcinoma")) return "Cancer";
  if (title.toLowerCase().includes("cancer")) return "Cancer";
  return "Other";
}

function extractTissue(title) {
  if (!title) return "Unknown";
  const t = title.toLowerCase();
  if (t.includes("breast")) return "Breast";
  if (t.includes("brain")) return "Brain";
  if (t.includes("lung")) return "Lung";
  return "Other";
}

function normalizeOmics(tech) {
  if (!tech) return "Other";
  const t = tech.toLowerCase();
  if (t.includes("exome")) return "WES";
  if (t.includes("rna")) return "Transcriptomics";
  if (t.includes("methylation")) return "Epigenomics";
  return "Other";
}