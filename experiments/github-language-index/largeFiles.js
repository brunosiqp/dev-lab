const fs = require("fs")
const path = require("path")

const MAX_SIZE_KB = 500
const largeFiles = []

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

      const sizeKB = stat.size / 1024

      if (sizeKB > MAX_SIZE_KB) {

        largeFiles.push({
          file: fullPath,
          sizeKB: sizeKB.toFixed(2)
        })

      }
    }
  }
}

scan(process.cwd())

const report = {
  thresholdKB: MAX_SIZE_KB,
  totalLargeFiles: largeFiles.length,
  files: largeFiles
}

if (!fs.existsSync("reports")) {
  fs.mkdirSync("reports")
}

fs.writeFileSync(
  "reports/large-files-report.json",
  JSON.stringify(report, null, 2)
)

console.log("Large files report generated")
console.log(report)