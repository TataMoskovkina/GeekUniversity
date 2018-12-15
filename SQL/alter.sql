#сначала изменим таблицу _countries

alter table _countries add primary key (country_id);

alter table _countries change country_id id int not null auto_increment;

alter table _countries drop title_ua;
alter table _countries drop title_be;
alter table _countries drop title_ru;
alter table _countries drop title_es;
alter table _countries drop title_pt;
alter table _countries drop title_de;
alter table _countries drop title_fr;
alter table _countries drop title_it;
alter table _countries drop title_pl;
alter table _countries drop title_ja;
alter table _countries drop title_lt;
alter table _countries drop title_lv;
alter table _countries drop title_cz;
alter table _countries change title_en title varchar(150) not null;
alter table _countries add index title_index (title);

#теперь изменим таблицу _regions

alter table _regions add primary key (region_id);

alter table _regions change region_id id int not null auto_increment;

alter table _regions add constraint region_to_country foreign key (country_id) references _countries(id) on delete cascade on update cascade;

alter table _regions drop title_ua;
alter table _regions drop title_be;
alter table _regions drop title_ru;
alter table _regions drop title_es;
alter table _regions drop title_pt;
alter table _regions drop title_de;
alter table _regions drop title_fr;
alter table _regions drop title_it;
alter table _regions drop title_pl;
alter table _regions drop title_ja;
alter table _regions drop title_lt;
alter table _regions drop title_lv;
alter table _regions drop title_cz;

alter table _regions change title_en title varchar(150) not null;

alter table _regions add index title_index (title);

#изменяем таблицу _cities

alter table _cities add primary key (city_id);

alter table _cities change city_id id int not null auto_increment;

alter table _cities add constraint city_to_country foreign key (country_id) references _countries(id) on delete cascade on update cascade;

alter table _cities add constraint city_to_region foreign key (region_id) references _regions(id) on delete cascade on update cascade;

alter table _cities drop title_ua;
alter table _cities drop title_be;
alter table _cities drop title_ru;
alter table _cities drop title_es;
alter table _cities drop title_pt;
alter table _cities drop title_de;
alter table _cities drop title_fr;
alter table _cities drop title_it;
alter table _cities drop title_pl;
alter table _cities drop title_ja;
alter table _cities drop title_lt;
alter table _cities drop title_lv;
alter table _cities drop title_cz;

alter table _cities drop area_ua;
alter table _cities drop area_be;
alter table _cities drop area_ru;
alter table _cities drop area_es;
alter table _cities drop area_pt;
alter table _cities drop area_de;
alter table _cities drop area_fr;
alter table _cities drop area_it;
alter table _cities drop area_pl;
alter table _cities drop area_ja;
alter table _cities drop area_lt;
alter table _cities drop area_lv;
alter table _cities drop area_cz;
alter table _cities drop area_en;

alter table _cities drop region_ua;
alter table _cities drop region_be;
alter table _cities drop region_ru;
alter table _cities drop region_es;
alter table _cities drop region_pt;
alter table _cities drop region_de;
alter table _cities drop region_fr;
alter table _cities drop region_it;
alter table _cities drop region_pl;
alter table _cities drop region_ja;
alter table _cities drop region_lt;
alter table _cities drop region_lv;
alter table _cities drop region_cz;
alter table _cities drop region_en;

alter table _cities change title_en title varchar(150) not null;

alter table _cities add index title_index (title);
