const fs = require("fs")
const path = require("path")
const languageMap = require("./languageMap")

const result = {}
let totalFiles = 0

function scan(dir) {

  const files = fs.readdirSync(dir)

  for (const file of files) {

    const fullPath = path.join(dir, file)
    const stat = fs.statSync(fullPath)

    if (stat.isDirectory()) {

      if (["node_modules", ".git", "dist", "build"].includes(file)) {
        continue
      }

      scan(fullPath)

    } else {

      totalFiles++

      const ext = path.extname(file)
      const lang = languageMap[ext] || "other"

      if (!result[lang]) result[lang] = 0
      result[lang]++
    }
  }
}

scan(process.cwd())

const report = {
  totalFiles,
  languages: result
}

fs.writeFileSync(
  "language-report.json",
  JSON.stringify(report, null, 2)
)

console.log("Language report generated")
console.log(report)