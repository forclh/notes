import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"

// 按需用 JS 回调覆盖 YAML 配置（必须在 loadQuartzConfig() 之前）
import * as ExternalPlugin from "./.quartz/plugins"

ExternalPlugin.Explorer({
  sortFn: (a, b) => {
    const ca = a.data?.frontmatter?.chapter ?? 99
    const cb = b.data?.frontmatter?.chapter ?? 99
    return ca - cb
  },
})

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
