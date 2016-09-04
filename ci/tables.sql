CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_admin` boolean NOT NULL DEFAULT False,
  `is_email_verify` boolean NOT NULL DEFAULT False,
  `reg_ip` varchar(30) NOT NULL DEFAULT '127.0.0.1',
  `referer_id` int(11) NOT NULL DEFAULT 0,
  `create_time` datetime,
  `update_time` datetime,
  `_created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `_updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  INDEX `referer_id` (`referer_id`)
);


CREATE TABLE `user_ss_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `port` int(11) NOT NULL,
  `password` varchar(10) NOT NULL,
  `create_time` datetime,
  `update_time` datetime,
  `_created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `_updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `port` (`port`)
);


CREATE TABLE `user_login_gift` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `login_gift` int(11) NOT NULL,
  `create_time` datetime,
  `update_time` datetime,
  `_created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `_updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
);


CREATE TABLE `user_total_traffic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `total_traffic` DECIMAL(15, 2) NOT NULL,
  `update_event` tinyint(4) NOT NULL DEFAULT 0,
  `create_time` datetime,
  `update_time` datetime,
  `_created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `_updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

