CREATE TABLE `toudoux`.`todo`
(
    `id`   UUID         NOT NULL DEFAULT uuid(),
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;
CREATE TABLE `toudoux`.`do`
(
    `id`      UUID         NOT NULL DEFAULT uuid(),
    `todo_id` UUID         NOT NULL,
    `title`   VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`todo_id`) REFERENCES `toudoux`.`todo` (`id`)
        ON DELETE CASCADE
) ENGINE = InnoDB;