const fs = require("fs")
const path = require("path")

const ignoreDirs = ["node_modules", ".git", "dist", "build"]

function generateTree(dir, prefix = "") {

  let tree = ""
  const files = fs.readdirSync(dir)

  files.forEach((file, index) => {

    if (ignoreDirs.includes(file)) return

    const fullPath = path.join(dir, file)
    const isLast = index === files.length - 1
    const connector = isLast ? "└── " : "├── "

    tree += prefix + connector + file + "\n"

    if (fs.statSync(fullPath).isDirectory()) {
      const newPrefix = prefix + (isLast ? "    " : "│   ")
      tree += generateTree(fullPath, newPrefix)
    }

  })

  return tree
}

const tree = generateTree(process.cwd())

if (!fs.existsSync("reports")) {
  fs.mkdirSync("reports")
}

fs.writeFileSync("reports/project-structure.txt", tree)

console.log("Project structure generated")
console.log(tree)