/* Create ISDB SQL Tables
	2-17-19
*/

create database isdb;
use isdb;

	create table User(
		username varchar(32) not null primary key,
		password varchar(32) not null
	);
	
	create table Song(
		sid int not null primary key auto_increment,
		Name varchar(64) not null,
		relDate varchar(32)
	);

	create table Artist(
		id int not null primary key auto_increment,
		Name varchar(64) not null
	);

	create table Album(
		aid int not null primary key auto_increment,
		Name varchar(64) not null,
		relDate varchar(32),
		numTracks int
	);

	create table SongAlb(
		sid int not null,
		aid int not null,
		primary key (sid, aid),
		foreign key (sid) references Song(sid),
		foreign key (aid) references Album(aid)
	);

	create table SongArt(
		sid int not null,
		id int not null,
		primary key (sid, id),
		foreign key (sid) references Song(sid),
		foreign key (id) references Artist(id)
	);

	create table AlbArt(
		aid int not null,
		id int not null,
		primary key (aid, id),
		foreign key (aid) references Album(aid),
		foreign key (id) references Artist(aid)
	);
