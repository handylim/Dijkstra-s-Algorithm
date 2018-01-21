<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Dijkstra's Algorithm</title>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.7/css/materialize.min.css" />
		<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.7/js/materialize.min.js"></script>
	</head>
	<body>
		<?php
			$json = json_decode(file_get_contents("result.json"));
			foreach ($json as $path):
		?>
			<div class="card horizontal">
				<h5>
					<i class="material-icons" style="font-size: 36px">router</i><br />
					<?php echo 'Router&nbsp;' . $path->from . '&nbsp;&nbsp;' ?>
				</h5>
				<table class="striped responsive-table" style="width: calc(100% - 110px)">
					<thead>
						<tr>
							<th>Destination</th>
							<th>Distance</th>
							<th>Next Hop</th>
						</tr>
					</thead>
					<tbody>
						<?php foreach($path->data as $data): ?>
							<tr>
								<td><?php echo $data->to ?></td>
								<td><?php echo $data->distance ?></td>
								<td><?php echo $data->next_hop ?></td>
							</tr>
						<?php endforeach ?>
					</tbody>
				</table>
			</div>
		<?php endforeach ?>
	</body>
</html>
