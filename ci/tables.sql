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
  UNIQUE KEY `email` (`email`)
);
