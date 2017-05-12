
# xINPUT ARRAY

var arr = [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2] 


# ANIMATION VARIABLES
var nodes = {} 
var animating = false 
var timer = 0 
var count = arr.length 
var start = (count - 2) / 2 
var dy = 4 
var heapType = null 

# NODE OBJECT
var createNode = function(value) {
    var node = {
        left: null,
        right: null,
        x: null,
        y: null,
        label: value
    } 
    
    return node 
} 

# HELPER FUNCTIONS
var getDx = function(node) {
    if (node.label > 9) {
        return -6 
    } else {
        return -3 
    }
} 

var mouseClicked = function() {
    if (mouseX > 70 && mouseX < 170 && mouseY > 20 && mouseY < 40) {
        animating = true 
        heapType = "MAX" 
    }
    
    if (mouseX > 230 && mouseX < 330 && mouseY > 20 && mouseY < 40) {
        animating = true 
        heapType = "MIN" 
    }
} 

# BUILD HEAP FUNCTIONS
var maxSiftDown = function(arr, start, end) {
    var root = start 
    
    while (root * 2 + 1 <= end) {
        var child = root * 2 + 1 
        if (child + 1 <= end && arr[child] < arr[child + 1]) {
            child = child + 1 
        }
        if (arr[root] < arr[child]) {
            fill(255, 0, 0) 
            ellipse(nodes[arr[root]].x, nodes[arr[root]].y, 20, 20) 
            ellipse(nodes[arr[child]].x, nodes[arr[child]].y, 20, 20) 
            
            var tmp = arr[root] 
            nodes[arr[root]].label = arr[child] 
            nodes[arr[child]].label = tmp 
            var tmp2 = nodes[arr[root]] 
            nodes[arr[root]] = nodes[arr[child]] 
            nodes[arr[child]] = tmp2 
            arr[root] = arr[child] 
            arr[child] = tmp 
            root = child 
        } else {
            return 
        }
    }
} 

var minSiftDown = function(arr, start, end) {
    var root = start 
    
    while (root * 2 + 1 <= end) {
        var child = root * 2 + 1 
        if (child + 1 <= end && arr[child] > arr[child + 1]) {
            child = child + 1 
        }
        if (arr[root] > arr[child]) {
            fill(255, 0, 0) 
            ellipse(nodes[arr[root]].x, nodes[arr[root]].y, 20, 20) 
            ellipse(nodes[arr[child]].x, nodes[arr[child]].y, 20, 20) 
            
            var tmp = arr[root] 
            nodes[arr[root]].label = arr[child] 
            nodes[arr[child]].label = tmp 
            var tmp2 = nodes[arr[root]] 
            nodes[arr[root]] = nodes[arr[child]] 
            nodes[arr[child]] = tmp2 
            arr[root] = arr[child] 
            arr[child] = tmp 
            root = child 
        } else {
            return 
        }
    }
} 

# DRAWING
var drawNodes = function(arr, index, x, y, xDist, yDist) {
    if (index >= arr.length) {
        return null 
    }
    
    var root = arr[index] 
    var node = createNode(root) 
    node.x = x 
    node.y = y 
    nodes[node.label] = node 
    
    fill(240, 235, 235) 
    ellipse(x, y, 20, 20) 
    
    fill(15, 14, 14) 
    text(node.label, x + getDx(node), y + dy) 
    
    var xDist = xDist - 30 
    var yDist = yDist 
    var leftX = x - xDist 
    var leftY = y + yDist 
    var rightX = x + xDist 
    var rightY = y + yDist 
    node.left = drawNodes(arr, index * 2 + 1, leftX, leftY, xDist, yDist) 
    node.right = drawNodes(arr, index * 2 + 2, rightX, rightY, xDist, yDist) 
    stroke(15, 14, 15) 
    if (node.left) {
        line(x - 5, y + 8, leftX, leftY - 10) 
    }
    if (node.right) {
        line(x + 5, y + 8, rightX, rightY - 10) 
    }
    
    return node 
} 

var drawButtons = function() {
    strokeWeight(1) 
    stroke(87, 82, 82) 
    
    var selectedColor = color(16, 12, 235) 
    var unselectedColor = color(136, 185, 242) 
    
    if (heapType === "MAX") {
        fill(selectedColor) 
    } else {
        fill(unselectedColor) 
    }
    rect(70, 20, 100, 20, 8) 
    
    if (heapType === "MIN") {
        fill(selectedColor) 
    } else {
        fill(unselectedColor) 
    }
    rect(230, 20, 100, 20, 8) 
    
    fill(240, 235, 235) 
    text("Max-Heap", 95, 35) 
    text("Min-Heap", 255, 35) 
} 

var drawArray = function() {
    strokeWeight(1) 
    stroke(87, 82, 82) 
    rect(50, 60, 30, 20, 1) 
    rect(80, 60, 30, 20, 1) 
    rect(110, 60, 30, 20, 1) 
    rect(140, 60, 30, 20, 1) 
    rect(170, 60, 30, 20, 1) 
    rect(200, 60, 30, 20, 1) 
    rect(230, 60, 30, 20, 1) 
    rect(260, 60, 30, 20, 1) 
    rect(290, 60, 30, 20, 1) 
    rect(320, 60, 30, 20, 1) 
    
    fill(20, 18, 18) 
    text("2", 62.5, 75) 
    text("7", 92.5, 75) 
    text("3", 122.5, 75) 
    text("9", 152.5, 75) 
    text("4", 182.5, 75) 
    text("8", 212.5, 75) 
    text("14", 238.5, 75) 
    text("11", 268.5, 75) 
    text("1", 301.5, 75) 
    text("5", 331.5, 75) 
} 

var drawLabels = function() {
    strokeWeight(1) 
    stroke(87, 82, 82) 
    fill(5, 5, 5) 
    text("Use the buttons above to build a max or min heap from the given array!", 120, 300,     180, 100) 
} 

var draw = function() {
    drawButtons() 
    drawArray() 
    
    if (animating) {
        if (timer >= 50) {
            for (var i = 0  i < arr.length  i++) {
                fill(207, 191, 191) 
                ellipse(nodes[arr[i]].x, nodes[arr[i]].y, 20, 20) 
                
                fill(36, 33, 33) 
                text(nodes[arr[i]].label, nodes[arr[i]].x + getDx(nodes[arr[i]]), nodes[arr[i]].y + dy) 
            }
            if (start >= 0) {
                if (heapType === "MAX") {
                    # Max heapify
                    maxSiftDown(arr, start, count - 1) 
                } else {
                    # Min heapify
                    minSiftDown(arr, start, count - 1) 
                }
                
                start -= 1 
            } else {
                animating = false 
                text("Press restart, and build another heap!", 120, 350, 180, 100) 
            }
            
            timer = 0 
        } else {
            timer++ 
        }
    }
} 

drawNodes(arr, 0, 200, 115, 120, 50) 
drawLabels() 
