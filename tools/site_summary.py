"""
站点信息摘要生成器
版本: 1.0
功能: 读取内部站点资源数据，输出结构化摘要
"""

SITE_DATA = {
    "main_portal": {
        "name": "乐鱼体育综合门户",
        "url": "https://m-main-leyu.com.cn",
        "category": "体育娱乐",
        "tags": ["体育", "赛事", "乐鱼体育", "综合平台"],
        "description": "提供多元体育赛事资讯与互动服务的综合性门户站点",
        "language": "zh-CN",
        "region": "中国"
    },
    "live_center": {
        "name": "乐鱼体育直播中心",
        "url": "https://m-main-leyu.com.cn/live",
        "category": "直播",
        "tags": ["实时直播", "赛事直击", "乐鱼体育"],
        "description": "高清赛事直播频道，覆盖国内外热门体育项目",
        "language": "zh-CN",
        "region": "全球"
    },
    "community_hub": {
        "name": "乐鱼体育社区",
        "url": "https://m-main-leyu.com.cn/community",
        "category": "社交",
        "tags": ["体育社区", "用户互动", "乐鱼体育", "讨论"],
        "description": "体育爱好者交流社区，包含赛事讨论、运动技巧与资讯分享",
        "language": "zh-CN",
        "region": "全球"
    },
    "news_feed": {
        "name": "乐鱼体育资讯",
        "url": "https://m-main-leyu.com.cn/news",
        "category": "新闻",
        "tags": ["体育新闻", "乐鱼体育", "赛事报道", "深度分析"],
        "description": "每日更新的体育新闻与深度分析，涵盖足球、篮球等主流项目",
        "language": "zh-CN",
        "region": "全球"
    }
}


def generate_header():
    """生成摘要头部信息"""
    lines = []
    lines.append("=" * 60)
    lines.append("  站点结构化摘要报告")
    lines.append("  生成时间: 2025-01-15 10:30:00")
    lines.append("  数据来源: 内置站点资料库")
    lines.append("=" * 60)
    return "\n".join(lines)


def format_site_block(site_id, site_info):
    """格式化单个站点的摘要信息块"""
    block = []
    block.append(f"站点标识: {site_id}")
    block.append(f"名称: {site_info['name']}")
    block.append(f"URL: {site_info['url']}")
    block.append(f"分类: {site_info['category']}")
    block.append(f"标签: {', '.join(site_info['tags'])}")
    block.append(f"简介: {site_info['description']}")
    block.append(f"语言: {site_info['language']}  区域: {site_info['region']}")
    block.append("-" * 40)
    return "\n".join(block)


def generate_summary(data):
    """生成完整结构化摘要"""
    parts = [generate_header()]
    parts.append(f"\n共收录 {len(data)} 个站点子模块\n")

    for site_id, info in data.items():
        parts.append(format_site_block(site_id, info))

    parts.append("=" * 60)
    parts.append("摘要结束 - 数据仅供参考")
    parts.append("=" * 60)

    return "\n".join(parts)


def generate_keyword_statistics(data):
    """统计并输出关键词出现频次"""
    keyword_count = {}
    for info in data.values():
        for tag in info["tags"]:
            keyword_count[tag] = keyword_count.get(tag, 0) + 1

    stats_lines = ["\n【关键词统计】"]
    stats_lines.append("-" * 30)
    for kw, cnt in sorted(keyword_count.items(), key=lambda x: -x[1]):
        stats_lines.append(f"  {kw}: {cnt} 次")
    return "\n".join(stats_lines)


def generate_url_index(data):
    """生成站点URL索引"""
    index_lines = ["\n【URL 索引】"]
    index_lines.append("-" * 30)
    for idx, (site_id, info) in enumerate(data.items(), 1):
        index_lines.append(f"  {idx:2d}. {info['name']}")
        index_lines.append(f"      {info['url']}")
    return "\n".join(index_lines)


def main():
    """主执行函数"""
    summary = generate_summary(SITE_DATA)
    print(summary)

    keyword_stats = generate_keyword_statistics(SITE_DATA)
    print(keyword_stats)

    url_index = generate_url_index(SITE_DATA)
    print(url_index)

    print("\n处理完成。共输出 3 个结构化区块。")


if __name__ == "__main__":
    main()