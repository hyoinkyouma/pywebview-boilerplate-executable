const systemInfo = document.getElementById("system-info")
const closeBtn = document.getElementById("close-btn")
const h1 = document.querySelector("h1")

const getSystemInfo = async () => {
    const systemInfoItems = JSON.parse(await pywebview.api.get_system_info())
    const systemInfoList = document.createElement("ul")
    Object.keys(systemInfoItems).forEach((key) => {
        const item = document.createElement("li")
        item.textContent = `${key.toUpperCase()}: ${systemInfoItems[key]}`
        systemInfoList.append(item)
    })
    systemInfo.textContent = ""
    systemInfo.append(systemInfoList)
}

const scaleEffect = ({timeout= 200}) => {
    setTimeout (() => {
        h1.classList.remove("scale-out")
    }, timeout)
    setTimeout(()=> {
        systemInfo.classList.remove("scale-out")
    }, timeout*2)
    setTimeout(()=> {
        closeBtn.classList.remove("scale-out")
    }, timeout*3)
}


const main = async () => {
    closeBtn.onclick = () => {
        pywebview.api.window_close()
    }
   await getSystemInfo()
   scaleEffect({timeout: 250})
}
window.addEventListener('pywebviewready', () => {
    main()
})
