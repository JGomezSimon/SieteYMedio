-- 1 Mostrar la Carta inicial mas repetida por cada jugador(mostrar nombre jugador y carta). 

select usuario.username, cartas.numero_carta
from usuario 
inner join jugador on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idusuario=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join cartas on turnos.carta_inicial=cartas.idcartas
GROUP BY username;


-- 2 Jugador que realiza la apuesta mas alta por partida. (Mostrar nombre jugador)

select nombre,max(apuesta),idpartida
from (select case 
when username is not null then usuario.username 
else descripcion 
end as nombre,max(turnos.apuesta) as apuesta,partida.idpartida as idpartida from jugador
left join bot on bot.idbot=jugador.idbot
left join usuario on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idjugador=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join partida on turnos.idpartida=partida.idpartida
where turnos.apuesta is not null
group by partida.idpartida,username
) tabla
where (apuesta,idpartida) in (

select 
max(turnos.apuesta),partida.idpartida  as apuesta from jugador
left join bot on bot.idbot=jugador.idbot
left join usuario on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idjugador=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join partida on turnos.idpartida=partida.idpartida
group by partida.idpartida
order by max(turnos.apuesta) desc
)
group by idpartida
order by idpartida;

-- 3 Jugador que realiza apuesta mas baja por partida. (Mostrar nombre jugador)


select nombre,min(apuesta),idpartida
from
(
select 
case 
when username is not null then usuario.username 
else descripcion 
end
as nombre,min(turnos.apuesta) as apuesta,partida.idpartida as idpartida from jugador
left join bot on bot.idbot=jugador.idbot
left join usuario on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idjugador=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join partida on turnos.idpartida=partida.idpartida
where turnos.apuesta is not null
group by partida.idpartida,username
) tabla
where (apuesta,idpartida) in (

select 
min(turnos.apuesta),partida.idpartida  as apuesta from jugador
left join bot on bot.idbot=jugador.idbot
left join usuario on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idjugador=participante.id_jugador
inner join turnos on participante.id_participante=turnos.idparticipante
inner join partida on turnos.idpartida=partida.idpartida
group by partida.idpartida
order by min(turnos.apuesta) desc
)
group by idpartida
order by idpartida;

-- 4 Ratio  de turnos ganados por jugador en cada partida (%),mostrar columna Nombre jugador, Nombre partida, nueva columna "porcentaje %"


select usuario.username, partida.nombre_sala, turnos.resultado, (turnos.idturnos/partida.idpartida)
from usuario
inner join jugador on usuario.idusuario=jugador.idusuario
inner join participante on jugador.idusuario=participante.id_jugador
inner join partida on participante.id_partida=partida.idpartida
inner join turnos on partida.idpartida=turnos.idpartida
where turnos.resultado like 'gana turno'


-- 5 Porcentaje de partidas ganadas Bots en general. Nueva columna "porcentaje %

select distinct bot.descripcion,partida.ganador_partida, truncate(((2/sum(partida.idpartida))*100),2) as porcentaje
from partida
inner join participante on partida.ganador_partida=participante.id_participante
inner join jugador on participante.id_jugador=jugador.idjugador
inner join bot on jugador.idbot=bot.idbot
where bot.idbot is not null


-- 6 Mostrar los datos de los jugadores y el tiempo que han durado sus partidas ganadas cuya puntuación obtenida es mayor que la media puntos de las partidas ganadas totales.
-- 7 Cuántas rondas se ganan en cada partida según el palo. Ejemplo: Partida 1 - 5 rondas - Bastos como carta inicial.

-- 8 Cuantas rondas gana la banca en cada partida.

select distinct partida.idpartida, participante.id_participante
from turnos
inner join partida on turnos.idpartida=partida.idpartida
inner join participante on partida.ganador_partida=participante.id_participante
inner join jugador on participante.id_jugador=jugador.idjugador
where turnos.es_banca like '1' 
order by partida.idpartida


-- 9 Cuántos usuarios han sido la banca en cada partida


SELECT partida.idpartida
from partida
inner join participante on partida.idpartida=participante.id_partida
inner join jugador on participante.id_jugador=jugador.idjugador
inner join usuario on jugador.idusuario=usuario.idusuario
inner join turnos on participante.id_participante=turnos.idparticipante
where turnos.es_banca like 1 group by turnos.es_banca


-- 10 Partida con la puntuación más alta final de todos los jugadores, mostrar nombre jugador, nombre partida,así como añadir una columna nueva en la que diga si ha ganado la partida o no.

select distinct usuario.username,bot.descripcion, partida.nombre_sala, partida.ganador_partida ,count(turnos.puntos_final) as puntuacion_final
from turnos
inner join partida on turnos.idpartida=partida.idpartida
inner join participante on partida.ganador_partida=participante.id_participante
inner join jugador on participante.id_jugador=jugador.idjugador
left join usuario on jugador.idusuario=usuario.idusuario
left join bot on jugador.idbot=bot.idbot
group by partida.idpartida

-- 11 Calcular la apuesta media por partida.

select partida.idpartida, truncate( avg(turnos.apuesta),2) As ApuestaMedia
from turnos
inner join partida on turnos.idpartida=partida.idpartida
inner join participante on partida.idpartida=participante.id_partida
inner join jugador on participante.id_jugador=jugador.idjugador
group by partida.idpartida


-- 12 Mostrar los datos de los usuarios que no son bot, así como cual ha sido su última apuesta en cada partida que ha jugado.

select distinct u.*,apuesta , max(t.numero_turno) as 'trurno_max', pd.idpartida
from usuario u 
inner join jugador j on u.idusuario = j.idusuario 
inner join participante p on j.idjugador = p.id_jugador 
inner join turnos t on p.id_participante = t.idparticipante 
inner join partida pd on pd.idpartida = t.idpartida 
group by idpartida,idparticipante
having numero_turno in  (select max(numero_turno) from turnos group by idpartida) 
order by t.idpartida asc,idparticipante asc, numero_turno asc


-- 13 Calcular el valor total de las cartas y el numero total de cartas que se han dado inicialmente en las manos en la partida. Por ejemplo, en la partida se han dado 50 cartas y el valor total de las cartas es 47,5.
select  idpartida AS partida,count(carta_inicial) AS numero_de_cartas, sum(valor) AS valor_total
from turnos, cartas
where carta_inicial=idcartas
group by idpartida;
-- 14 Diferencia de puntos de los participantes de las partidas entre la ronda 1 y 5. Ejemplo: Rafa tenia 20 puntos, en la ronda 5 tiene 15, tiene -5 puntos de diferencia.
