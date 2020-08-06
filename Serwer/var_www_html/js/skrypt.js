async function myFunction() {
  const x = document.getElementById("b1");
  const xd = await fetch("https://pokeapi.co/api/v2/pokemon/ditto/");
  const xdd = await xd.text();
  if (x.innerHTML === "CLICK ME_") {
    x.innerHTML = "NICE";
    x.style.background = '#000000';
    console.log(xdd);
  }
  else {
    x.innerHTML = "CLICK ME_";
    x.style.background = '#ff0000';
    var jsontext = '{ "name":"John", "age":30, "city":"New York"}';
    var obj = JSON.parse(jsontext);
    console.log(JSON.stringify(obj));
  }
}

async function myFunction2() {
  const button2_id = document.getElementById("b2");
  const php_script = await fetch("XD.php");
  const php_log = await php_script.text();
  console.log(php_log);
}

async function clearEpaper(){
  const button_clear_epaper = document.getElementById("b_clear");
  const php_script = await fetch("clear.php");
  const php_log = await php_script.text();
  console.log(php_log);
}

async function sendToEpaper(){
  const button_send_epaper = document.getElementById("b_send_epaper");
  const text_field = document.getElementById("text_field");
  button_send_epaper.innerHTML = "Sending...";
  console.log(text_field.value);
  const php_url = "send_text_epaper.php?text='" + text_field.value + "'";
  const php_script = await fetch(php_url);
  const php_log = await php_script.text();
  console.log(php_log);
  button_send_epaper.innerHTML = "SEND TEXT TO E-PAPER";
}

async function showDataEpaper(){
  const button_show_data_epaper = document.getElementById("b_show_data_epaper");
  button_show_data_epaper.innerHTML = "Please wait...";
  const php_script = await fetch("epaper_show.php");
  const php_log = await php_script.text();
  console.log(php_log);
  button_show_data_epaper.innerHTML = "SHOW DATA ON E-PAPER";
}

async function showData(){
  const button_show_data = document.getElementById("b_show_data");
  const data = await fetch("https://api.thingspeak.com/channels/775759/feeds.json?results=1");
  const data_log = await data.text();
  // console.log(data_log);

  var data_json = JSON.parse(data_log);
  console.log(data_json);

  const t1_n = document.getElementById("t1_n");
  const t1_v = document.getElementById("t1_v");
  const t1_u = document.getElementById("t1_u");
  const t2_n = document.getElementById("t2_n");
  const t2_v = document.getElementById("t2_v");
  const t2_u = document.getElementById("t2_u");
  const t3_n = document.getElementById("t3_n");
  const t3_v = document.getElementById("t3_v");
  const t3_u = document.getElementById("t3_u");
  const t4_n = document.getElementById("t4_n");
  const t4_v = document.getElementById("t4_v");
  const t4_u = document.getElementById("t4_u");
  const t5_n = document.getElementById("t5_n");
  const t5_v = document.getElementById("t5_v");
  const t5_u = document.getElementById("t5_u");
  const t6_n = document.getElementById("t6_n");
  const t6_v = document.getElementById("t6_v");
  const t6_u = document.getElementById("t6_u");
  const t7_n = document.getElementById("t7_n");
  const t7_v = document.getElementById("t7_v");
  const t7_u = document.getElementById("t7_u");
  const t8_n = document.getElementById("t8_n");
  const t8_v = document.getElementById("t8_v");
  const t8_u = document.getElementById("t8_u");
  const t9_n = document.getElementById("t9_n");
  const t9_v = document.getElementById("t9_v");
  const t9_u = document.getElementById("t9_u");

  t1_n.innerHTML = data_json.channel.field1
  t2_n.innerHTML = data_json.channel.field2
  t3_n.innerHTML = data_json.channel.field3
  t4_n.innerHTML = data_json.channel.field4
  t5_n.innerHTML = data_json.channel.field5
  t6_n.innerHTML = data_json.channel.field6
  t7_n.innerHTML = data_json.channel.field7
  t8_n.innerHTML = data_json.channel.field8

  t1_v.innerHTML = data_json.feeds[0].field1
  t2_v.innerHTML = data_json.feeds[0].field2
  t3_v.innerHTML = data_json.feeds[0].field3
  t4_v.innerHTML = data_json.feeds[0].field4
  t5_v.innerHTML = data_json.feeds[0].field5
  t6_v.innerHTML = data_json.feeds[0].field6
  t7_v.innerHTML = data_json.feeds[0].field7
  t8_v.innerHTML = data_json.feeds[0].field8

  t1_u.innerHTML = "*C"
  t2_u.innerHTML = "hPa"
  t3_u.innerHTML = "%"
  t4_u.innerHTML = "ug/m3"
  t5_u.innerHTML = "ug/m3"
  t6_u.innerHTML = "ug/m3"
  t7_u.innerHTML = "-"
  t8_u.innerHTML = "-"

  const name = document.getElementById("station_name");
  const id = document.getElementById("station_id");
  name.innerHTML = "Name: " + data_json.channel.name
  id.innerHTML = "ID: " + data_json.channel.id
}

async function showDistance(){
  const button_show_distance = document.getElementById("b_distance");
  const text_distance = document.getElementById("distance");
  button_show_distance.innerHTML = "Please wait...";
  const php_script = await fetch("distance.php");
  const php_log = await php_script.text();
  console.log(php_log);
  text_distance.innerHTML = php_log + " cm";
  button_show_distance.innerHTML = "SHOW DISTANCE";
}