let a = [1,2,3,4,5,6,7,8,9,0];
let b = ["một","hai","ba","bốn","năm","sáu","bảy","tám","chín","mười"];
let c = [];
let daySo = prompt("Nhập vào dãy số");
let arr = [];
let  index_a = 0;
arr = daySo.split("")
for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < a.length; j++) {
        if (arr[i] == a[j]){
            index_a = j;
        }
    }
    c.push(b[index_a]);

}
document.write(c.join(' '))