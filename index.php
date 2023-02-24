<!DOCTYPE html>
	<head>
		<title>Plant Care System Server</title>
				
		
	</head>
	<body>
		
		<h1> Plant Care System Server </h1>
		<h2> Commands </h2>
		<h3><a href="/action1" > Watering </a></h3>
		<h3><a href="/action2" > Stop Watering </a></h3>
		<h3><a href="/action3" > Play Buzzer </a></h3>
		
		<h1> Table of Data </h1>
		<p><a href="/action4" > Update Table </a></p>
		<table border = "1">
				<tr>
					<th>Activity ID</th>
					<th>Date</th>
					<th>Time</th>
					<th>Humidity</th>
					<th>Temparature</th>
					<th>Shocked</th>
					<th>Watering</th>
				</tr>
				{% for pin in pins1 %}
				<tr>							
					<td>{{pin[0]}}</td>
					<td>{{pin[1]}}</td>
					<td>{{pin[2]}}</td>
					<td>{{pin[3]}}</td>
					<td>{{pin[4]}}</td>
					<td>{{pin[5]}}</td>
					<td>{{pin[6]}}</td>
				</tr>
				{% endfor %}
				</table>
				
	
		<!--<h2> Toggle buttons </h2>
		{% for pin in pins %}
			<h3>{{ pins[pin].name }}
			{% if pins[pin].state == 1 %}
				is currently <strong>on</strong></h3>
				<div class="row"><div class="col-md-2">
				<a href="/{{pin}}/off" class="btn btn-block btn-lg btndefault" role="button">Turn off</a>
				</div></div>
			{% else %}
				is currently <strong>off</strong></h3>
				<div class="row"><div class="col-md-2">
				<a href="/{{pin}}/on" class="btn btn-block btn-lg btn-primary"
role="button">Turn on</a>
				</div></div>
			{% endif %}
		{% endfor %}-->
	</body>
</html>
