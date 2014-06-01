-- MySQL dump 10.13  Distrib 5.1.44, for Win32 (ia32)
--
-- Host: localhost    Database: app_mese2014
-- ------------------------------------------------------
-- Server version	5.1.44-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_company`
--

DROP TABLE IF EXISTS `accounts_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(255) NOT NULL,
  `assets` decimal(15,4) NOT NULL,
  `description` longtext NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_company`
--

/*!40000 ALTER TABLE `accounts_company` DISABLE KEYS */;
INSERT INTO `accounts_company` VALUES (1,'','0.0000','','');
/*!40000 ALTER TABLE `accounts_company` ENABLE KEYS */;

--
-- Table structure for table `accounts_company_financial_reports`
--

DROP TABLE IF EXISTS `accounts_company_financial_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_company_financial_reports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) NOT NULL,
  `privatefile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `company_id` (`company_id`,`privatefile_id`),
  KEY `accounts_company_financial_reports_0316dde1` (`company_id`),
  KEY `accounts_company_financial_reports_51d6352d` (`privatefile_id`),
  CONSTRAINT `company_id_refs_id_788556b5` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_company_financial_reports`
--

/*!40000 ALTER TABLE `accounts_company_financial_reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_company_financial_reports` ENABLE KEYS */;

--
-- Table structure for table `accounts_financialinstitution`
--

DROP TABLE IF EXISTS `accounts_financialinstitution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_financialinstitution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(255) NOT NULL,
  `assets` decimal(15,4) NOT NULL,
  `description` longtext NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `type` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_financialinstitution`
--

/*!40000 ALTER TABLE `accounts_financialinstitution` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_financialinstitution` ENABLE KEYS */;

--
-- Table structure for table `accounts_person`
--

DROP TABLE IF EXISTS `accounts_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(255) NOT NULL,
  `assets` decimal(15,4) NOT NULL,
  `fixed_assets` decimal(15,4) NOT NULL,
  `company_type_id` int(11) DEFAULT NULL,
  `company_object_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_person_a3c9d75e` (`company_type_id`),
  CONSTRAINT `company_type_id_refs_id_2a440fb2` FOREIGN KEY (`company_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_person`
--

/*!40000 ALTER TABLE `accounts_person` DISABLE KEYS */;
INSERT INTO `accounts_person` VALUES (1,'','10000.0000','0.0000',9,1),(2,'','10000.0000','0.0000',9,1);
/*!40000 ALTER TABLE `accounts_person` ENABLE KEYS */;

--
-- Table structure for table `accounts_person_consumption_reports`
--

DROP TABLE IF EXISTS `accounts_person_consumption_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_person_consumption_reports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `privatefile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`,`privatefile_id`),
  KEY `accounts_person_consumption_reports_16f39487` (`person_id`),
  KEY `accounts_person_consumption_reports_51d6352d` (`privatefile_id`),
  CONSTRAINT `person_id_refs_id_3293187b` FOREIGN KEY (`person_id`) REFERENCES `accounts_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_person_consumption_reports`
--

/*!40000 ALTER TABLE `accounts_person_consumption_reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_person_consumption_reports` ENABLE KEYS */;

--
-- Table structure for table `accounts_person_debt_files`
--

DROP TABLE IF EXISTS `accounts_person_debt_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_person_debt_files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `privatefile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`,`privatefile_id`),
  KEY `accounts_person_debt_files_16f39487` (`person_id`),
  KEY `accounts_person_debt_files_51d6352d` (`privatefile_id`),
  CONSTRAINT `person_id_refs_id_8f18917a` FOREIGN KEY (`person_id`) REFERENCES `accounts_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_person_debt_files`
--

/*!40000 ALTER TABLE `accounts_person_debt_files` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_person_debt_files` ENABLE KEYS */;

--
-- Table structure for table `accounts_userprofile`
--

DROP TABLE IF EXISTS `accounts_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `info_type_id` int(11) DEFAULT NULL,
  `info_object_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `accounts_userprofile_f556c310` (`info_type_id`),
  CONSTRAINT `info_type_id_refs_id_b3580da9` FOREIGN KEY (`info_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_a240fa0c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile`
--

/*!40000 ALTER TABLE `accounts_userprofile` DISABLE KEYS */;
INSERT INTO `accounts_userprofile` VALUES (1,2,9,1),(2,3,8,1),(3,4,8,2),(4,1,NULL,NULL);
/*!40000 ALTER TABLE `accounts_userprofile` ENABLE KEYS */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add log entry',6,'add_logentry'),(17,'Can change log entry',6,'change_logentry'),(18,'Can delete log entry',6,'delete_logentry'),(19,'Can add user profile',7,'add_userprofile'),(20,'Can change user profile',7,'change_userprofile'),(21,'Can delete user profile',7,'delete_userprofile'),(22,'Can add person',8,'add_person'),(23,'Can change person',8,'change_person'),(24,'Can delete person',8,'delete_person'),(25,'Can add company',9,'add_company'),(26,'Can change company',9,'change_company'),(27,'Can delete company',9,'delete_company'),(28,'Can add financial institution',10,'add_financialinstitution'),(29,'Can change financial institution',10,'change_financialinstitution'),(30,'Can delete financial institution',10,'delete_financialinstitution'),(31,'Can add bank',10,'add_bank'),(32,'Can change bank',10,'change_bank'),(33,'Can delete bank',10,'delete_bank'),(34,'Can add fund company',10,'add_fundcompany'),(35,'Can change fund company',10,'change_fundcompany'),(36,'Can delete fund company',10,'delete_fundcompany'),(37,'Can add passage',13,'add_passage'),(38,'Can change passage',13,'change_passage'),(39,'Can delete passage',13,'delete_passage'),(40,'Can add comment',14,'add_comment'),(41,'Can change comment',14,'change_comment'),(42,'Can delete comment',14,'delete_comment'),(43,'Can add file',15,'add_file'),(44,'Can change file',15,'change_file'),(45,'Can delete file',15,'delete_file'),(46,'Can add public file',15,'add_publicfile'),(47,'Can change public file',15,'change_publicfile'),(48,'Can delete public file',15,'delete_publicfile'),(49,'Can add private file',15,'add_privatefile'),(50,'Can change private file',15,'change_privatefile'),(51,'Can delete private file',15,'delete_privatefile'),(52,'Can add fund',18,'add_fund'),(53,'Can change fund',18,'change_fund'),(54,'Can delete fund',18,'delete_fund'),(55,'Can add share',19,'add_share'),(56,'Can change share',19,'change_share'),(57,'Can delete share',19,'delete_share'),(58,'Can add log',20,'add_log'),(59,'Can change log',20,'change_log'),(60,'Can delete log',20,'delete_log'),(61,'Can add stock',21,'add_stock'),(62,'Can change stock',21,'change_stock'),(63,'Can delete stock',21,'delete_stock'),(64,'Can add share',22,'add_share'),(65,'Can change share',22,'change_share'),(66,'Can delete share',22,'delete_share'),(67,'Can add log',23,'add_log'),(68,'Can change log',23,'change_log'),(69,'Can delete log',23,'delete_log'),(70,'Can add future',24,'add_future'),(71,'Can change future',24,'change_future'),(72,'Can delete future',24,'delete_future'),(73,'Can add share',25,'add_share'),(74,'Can change share',25,'change_share'),(75,'Can delete share',25,'delete_share'),(76,'Can add log',26,'add_log'),(77,'Can change log',26,'change_log'),(78,'Can delete log',26,'delete_log'),(79,'Can add trade log',27,'add_tradelog'),(80,'Can change trade log',27,'change_tradelog'),(81,'Can delete trade log',27,'delete_tradelog'),(82,'Can add bond',28,'add_bond'),(83,'Can change bond',28,'change_bond'),(84,'Can delete bond',28,'delete_bond'),(85,'Can add share',29,'add_share'),(86,'Can change share',29,'change_share'),(87,'Can delete share',29,'delete_share'),(88,'Can add log',30,'add_log'),(89,'Can change log',30,'change_log'),(90,'Can delete log',30,'delete_log');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$GPSqqP0KGZRx$o4Ss2GmumklyO1C4B2lH/hybvfrg1annkA5MeNHlm1M=','2014-05-17 23:41:55',1,'superuser','','','',1,1,'2014-05-17 23:39:47'),(2,'pbkdf2_sha256$10000$n4Dv1hmVxPs6$PLxUj/UlN4Rth5INnAfvA17FK3iaGNx2J4f0AznY0ZM=','2014-05-17 23:41:42',0,'cpy','','','',0,1,'2014-05-17 23:41:42'),(3,'pbkdf2_sha256$10000$JoYixUMnZdy8$ZEkUMb/UubZXGVTarpl58uRRksix/pNpW402jRqOJhQ=','2014-05-17 23:41:43',0,'test','','','',0,1,'2014-05-17 23:41:43'),(4,'pbkdf2_sha256$10000$hYeBgiTR0Ytr$4Iba5RyI1ZvATzgSyhKPfdYnYttQqyn5nK+Gmsf3OrA=','2014-05-17 23:41:43',0,'test2','','','',0,1,'2014-05-17 23:41:43');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

--
-- Table structure for table `bonds_bond`
--

DROP TABLE IF EXISTS `bonds_bond`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bonds_bond` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(20) NOT NULL,
  `total_shares` decimal(15,4) NOT NULL,
  `enterprise_object_id` int(10) unsigned NOT NULL,
  `enterprise_type_id` int(11) NOT NULL,
  `current_price` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `display_name` (`display_name`),
  KEY `bonds_bond_b6c026a6` (`enterprise_type_id`),
  CONSTRAINT `enterprise_type_id_refs_id_e5ac30fb` FOREIGN KEY (`enterprise_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bonds_bond`
--

/*!40000 ALTER TABLE `bonds_bond` DISABLE KEYS */;
/*!40000 ALTER TABLE `bonds_bond` ENABLE KEYS */;

--
-- Table structure for table `bonds_log`
--

DROP TABLE IF EXISTS `bonds_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bonds_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(5) NOT NULL,
  `fond_id` int(11) NOT NULL,
  `beginning_price` decimal(15,4) NOT NULL,
  `last_final_price` decimal(15,4) NOT NULL,
  `highest_price` decimal(15,4) NOT NULL,
  `lowest_price` decimal(15,4) NOT NULL,
  `final_price` decimal(15,4) NOT NULL,
  `transcation_quantity` decimal(15,4) NOT NULL,
  `transcation_money` decimal(15,4) NOT NULL,
  `increasement` decimal(15,4) NOT NULL,
  `increased_rate` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bonds_log_ac3dae63` (`fond_id`),
  CONSTRAINT `fond_id_refs_id_b0999e2e` FOREIGN KEY (`fond_id`) REFERENCES `bonds_bond` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bonds_log`
--

/*!40000 ALTER TABLE `bonds_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `bonds_log` ENABLE KEYS */;

--
-- Table structure for table `bonds_share`
--

DROP TABLE IF EXISTS `bonds_share`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bonds_share` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shares` decimal(15,4) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `fond_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bonds_share_cb902d83` (`owner_id`),
  KEY `bonds_share_ac3dae63` (`fond_id`),
  CONSTRAINT `fond_id_refs_id_46d8f579` FOREIGN KEY (`fond_id`) REFERENCES `bonds_bond` (`id`),
  CONSTRAINT `owner_id_refs_id_feb70ad1` FOREIGN KEY (`owner_id`) REFERENCES `accounts_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bonds_share`
--

/*!40000 ALTER TABLE `bonds_share` DISABLE KEYS */;
/*!40000 ALTER TABLE `bonds_share` ENABLE KEYS */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'log entry','admin','logentry'),(7,'user profile','accounts','userprofile'),(8,'person','accounts','person'),(9,'company','accounts','company'),(10,'financial institution','accounts','financialinstitution'),(11,'fund company','accounts','fundcompany'),(12,'bank','accounts','bank'),(13,'passage','webboard','passage'),(14,'comment','webboard','comment'),(15,'file','file_upload','file'),(16,'private file','file_upload','privatefile'),(17,'public file','file_upload','publicfile'),(18,'fund','funds','fund'),(19,'share','funds','share'),(20,'log','funds','log'),(21,'stock','stocks','stock'),(22,'share','stocks','share'),(23,'log','stocks','log'),(24,'future','futures','future'),(25,'share','futures','share'),(26,'log','futures','log'),(27,'trade log','logs','tradelog'),(28,'bond','bonds','bond'),(29,'share','bonds','share'),(30,'log','bonds','log');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('bc7co2g870r0rbk9l5709liem5txxppt','ZTlkMmNhNWJmNGI3NWQ1MWZjYTk2NTE2ZTc3YjAxZjg5NjMwYTkwNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-05-31 23:41:55');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

--
-- Table structure for table `file_upload_file`
--

DROP TABLE IF EXISTS `file_upload_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `file_upload_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime NOT NULL,
  `file` varchar(100) NOT NULL,
  `file_type` varchar(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file_upload_file`
--

/*!40000 ALTER TABLE `file_upload_file` DISABLE KEYS */;
/*!40000 ALTER TABLE `file_upload_file` ENABLE KEYS */;

--
-- Table structure for table `funds_fund`
--

DROP TABLE IF EXISTS `funds_fund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funds_fund` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(20) NOT NULL,
  `total_shares` decimal(15,4) NOT NULL,
  `enterprise_object_id` int(10) unsigned NOT NULL,
  `enterprise_type_id` int(11) NOT NULL,
  `unit_net_worth` decimal(15,4) NOT NULL,
  `total_net_worth` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `display_name` (`display_name`),
  KEY `funds_fund_b6c026a6` (`enterprise_type_id`),
  CONSTRAINT `enterprise_type_id_refs_id_5f61e5eb` FOREIGN KEY (`enterprise_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funds_fund`
--

/*!40000 ALTER TABLE `funds_fund` DISABLE KEYS */;
/*!40000 ALTER TABLE `funds_fund` ENABLE KEYS */;

--
-- Table structure for table `funds_log`
--

DROP TABLE IF EXISTS `funds_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funds_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(5) NOT NULL,
  `fond_id` int(11) NOT NULL,
  `last_final_price` decimal(15,4) NOT NULL,
  `increasement` decimal(15,4) NOT NULL,
  `increased_rate` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `funds_log_ac3dae63` (`fond_id`),
  CONSTRAINT `fond_id_refs_id_a136d66c` FOREIGN KEY (`fond_id`) REFERENCES `funds_fund` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funds_log`
--

/*!40000 ALTER TABLE `funds_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `funds_log` ENABLE KEYS */;

--
-- Table structure for table `funds_share`
--

DROP TABLE IF EXISTS `funds_share`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funds_share` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shares` decimal(15,4) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `fond_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `funds_share_cb902d83` (`owner_id`),
  KEY `funds_share_ac3dae63` (`fond_id`),
  CONSTRAINT `fond_id_refs_id_5045f3de` FOREIGN KEY (`fond_id`) REFERENCES `funds_fund` (`id`),
  CONSTRAINT `owner_id_refs_id_b2f6e169` FOREIGN KEY (`owner_id`) REFERENCES `accounts_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funds_share`
--

/*!40000 ALTER TABLE `funds_share` DISABLE KEYS */;
/*!40000 ALTER TABLE `funds_share` ENABLE KEYS */;

--
-- Table structure for table `futures_future`
--

DROP TABLE IF EXISTS `futures_future`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `futures_future` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(20) NOT NULL,
  `total_shares` decimal(15,4) NOT NULL,
  `enterprise_object_id` int(10) unsigned NOT NULL,
  `enterprise_type_id` int(11) NOT NULL,
  `current_price` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `display_name` (`display_name`),
  KEY `futures_future_b6c026a6` (`enterprise_type_id`),
  CONSTRAINT `enterprise_type_id_refs_id_47f5189c` FOREIGN KEY (`enterprise_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `futures_future`
--

/*!40000 ALTER TABLE `futures_future` DISABLE KEYS */;
/*!40000 ALTER TABLE `futures_future` ENABLE KEYS */;

--
-- Table structure for table `futures_log`
--

DROP TABLE IF EXISTS `futures_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `futures_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(5) NOT NULL,
  `fond_id` int(11) NOT NULL,
  `beginning_price` decimal(15,4) NOT NULL,
  `last_final_price` decimal(15,4) NOT NULL,
  `highest_price` decimal(15,4) NOT NULL,
  `lowest_price` decimal(15,4) NOT NULL,
  `final_price` decimal(15,4) NOT NULL,
  `transcation_quantity` decimal(15,4) NOT NULL,
  `transcation_money` decimal(15,4) NOT NULL,
  `increasement` decimal(15,4) NOT NULL,
  `increased_rate` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `futures_log_ac3dae63` (`fond_id`),
  CONSTRAINT `fond_id_refs_id_5f5b49a1` FOREIGN KEY (`fond_id`) REFERENCES `futures_future` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `futures_log`
--

/*!40000 ALTER TABLE `futures_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `futures_log` ENABLE KEYS */;

--
-- Table structure for table `futures_share`
--

DROP TABLE IF EXISTS `futures_share`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `futures_share` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shares` decimal(15,4) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `fond_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `futures_share_cb902d83` (`owner_id`),
  KEY `futures_share_ac3dae63` (`fond_id`),
  CONSTRAINT `fond_id_refs_id_5ab1ff0b` FOREIGN KEY (`fond_id`) REFERENCES `futures_future` (`id`),
  CONSTRAINT `owner_id_refs_id_282242eb` FOREIGN KEY (`owner_id`) REFERENCES `accounts_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `futures_share`
--

/*!40000 ALTER TABLE `futures_share` DISABLE KEYS */;
/*!40000 ALTER TABLE `futures_share` ENABLE KEYS */;

--
-- Table structure for table `logs_tradelog`
--

DROP TABLE IF EXISTS `logs_tradelog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logs_tradelog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_id` int(11) NOT NULL,
  `action` varchar(4) NOT NULL,
  `fond_type_id` int(11) NOT NULL,
  `fond_object_id` int(10) unsigned NOT NULL,
  `quantity` decimal(15,4) NOT NULL,
  `money` decimal(15,4) NOT NULL,
  `operated_time` datetime NOT NULL,
  `year` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `logs_tradelog_cb902d83` (`owner_id`),
  KEY `logs_tradelog_4474ba6c` (`fond_type_id`),
  CONSTRAINT `fond_type_id_refs_id_01963d0c` FOREIGN KEY (`fond_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `owner_id_refs_id_18012e98` FOREIGN KEY (`owner_id`) REFERENCES `accounts_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logs_tradelog`
--

/*!40000 ALTER TABLE `logs_tradelog` DISABLE KEYS */;
/*!40000 ALTER TABLE `logs_tradelog` ENABLE KEYS */;

--
-- Table structure for table `stocks_log`
--

DROP TABLE IF EXISTS `stocks_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stocks_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(5) NOT NULL,
  `fond_id` int(11) NOT NULL,
  `beginning_price` decimal(15,4) NOT NULL,
  `last_final_price` decimal(15,4) NOT NULL,
  `highest_price` decimal(15,4) NOT NULL,
  `lowest_price` decimal(15,4) NOT NULL,
  `final_price` decimal(15,4) NOT NULL,
  `transcation_quantity` decimal(15,4) NOT NULL,
  `transcation_money` decimal(15,4) NOT NULL,
  `increasement` decimal(15,4) NOT NULL,
  `increased_rate` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stocks_log_ac3dae63` (`fond_id`),
  CONSTRAINT `fond_id_refs_id_e02f135a` FOREIGN KEY (`fond_id`) REFERENCES `stocks_stock` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks_log`
--

/*!40000 ALTER TABLE `stocks_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `stocks_log` ENABLE KEYS */;

--
-- Table structure for table `stocks_share`
--

DROP TABLE IF EXISTS `stocks_share`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stocks_share` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shares` decimal(15,4) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `fond_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stocks_share_cb902d83` (`owner_id`),
  KEY `stocks_share_ac3dae63` (`fond_id`),
  CONSTRAINT `fond_id_refs_id_14b2e948` FOREIGN KEY (`fond_id`) REFERENCES `stocks_stock` (`id`),
  CONSTRAINT `owner_id_refs_id_2e66c564` FOREIGN KEY (`owner_id`) REFERENCES `accounts_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks_share`
--

/*!40000 ALTER TABLE `stocks_share` DISABLE KEYS */;
/*!40000 ALTER TABLE `stocks_share` ENABLE KEYS */;

--
-- Table structure for table `stocks_stock`
--

DROP TABLE IF EXISTS `stocks_stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stocks_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(20) NOT NULL,
  `total_shares` decimal(15,4) NOT NULL,
  `enterprise_object_id` int(10) unsigned NOT NULL,
  `enterprise_type_id` int(11) NOT NULL,
  `current_price` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `display_name` (`display_name`),
  KEY `stocks_stock_b6c026a6` (`enterprise_type_id`),
  CONSTRAINT `enterprise_type_id_refs_id_e629e857` FOREIGN KEY (`enterprise_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks_stock`
--

/*!40000 ALTER TABLE `stocks_stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `stocks_stock` ENABLE KEYS */;

--
-- Table structure for table `webboard_comment`
--

DROP TABLE IF EXISTS `webboard_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webboard_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `author_id` int(11) NOT NULL,
  `created_time` datetime NOT NULL,
  `passage_id` int(11) NOT NULL,
  `respond_comment_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `webboard_comment_e969df21` (`author_id`),
  KEY `webboard_comment_e215af53` (`passage_id`),
  KEY `webboard_comment_57d05f33` (`respond_comment_id`),
  CONSTRAINT `author_id_refs_id_6e715fa5` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `passage_id_refs_id_a7611baa` FOREIGN KEY (`passage_id`) REFERENCES `webboard_passage` (`id`),
  CONSTRAINT `respond_comment_id_refs_id_08dafbad` FOREIGN KEY (`respond_comment_id`) REFERENCES `webboard_comment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webboard_comment`
--

/*!40000 ALTER TABLE `webboard_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `webboard_comment` ENABLE KEYS */;

--
-- Table structure for table `webboard_passage`
--

DROP TABLE IF EXISTS `webboard_passage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webboard_passage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(3) NOT NULL,
  `title` varchar(255) NOT NULL,
  `created_time` datetime NOT NULL,
  `year` varchar(5) NOT NULL,
  `author_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `webboard_passage_e969df21` (`author_id`),
  CONSTRAINT `author_id_refs_id_d4b3e522` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webboard_passage`
--

/*!40000 ALTER TABLE `webboard_passage` DISABLE KEYS */;
INSERT INTO `webboard_passage` VALUES (1,'MED','Lorem ipsum','2014-05-17 23:43:59','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(2,'MED','Lorem ipsum2','2014-05-17 23:44:11','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(3,'MED','Lorem ipsum3','2014-05-17 23:44:15','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(4,'MED','Lorem ipsum4','2014-05-17 23:44:19','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(5,'MED','Lorem ipsum5','2014-05-17 23:44:24','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(6,'MED','Lorem ipsum6','2014-05-17 23:44:29','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(7,'MED','Lorem ipsum7','2014-05-17 23:44:32','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(8,'MED','Lorem ipsum8','2014-05-17 23:44:36','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(9,'MED','Lorem ipsum9','2014-05-17 23:44:40','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(10,'MED','Lorem ipsum10','2014-05-17 23:44:45','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(11,'MED','Lorem ipsum11','2014-05-17 23:44:48','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(12,'MED','Lorem ipsum12','2014-05-17 23:44:55','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(13,'MED','Lorem ipsum13','2014-05-17 23:44:59','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(14,'MED','Lorem ipsum14','2014-05-17 23:45:03','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'),(15,'MED','Lorem ipsum15','2014-05-17 23:45:06','20141',1,'<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>');
/*!40000 ALTER TABLE `webboard_passage` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-05-17 23:47:05
