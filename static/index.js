console.log("WORKING")

let no=6
document.getElementById("addNews").onclick = function() {
    if(no<=25)
    {
        var newsCell = document.getElementById("newsCell");
        var input = document.createElement("input");
        input.type = "text";
        input.name='input_text[]'
        input.id='newsbox'
        input.placeholder="Enter News"
        input.required="True"
        var label=document.createElement("label");
        label.textContent='News '+no +': ';
        no++;
        var br = document.createElement("br");
        newsCell.appendChild(label);
        newsCell.appendChild(input);
        newsCell.appendChild(br);
    }
}
document.getElementById("removeNews").onclick= function() {
    if (no>6)
    {
        document.getElementById("newsCell").lastChild.remove(); 
        document.getElementById("newsCell").lastChild.remove();
        document.getElementById("newsCell").lastChild.remove();
        no--;
    }
  }
