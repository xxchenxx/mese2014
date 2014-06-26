-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: app_mese2014
-- ------------------------------------------------------
-- Server version	5.5.37-0ubuntu0.14.04.1

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
-- Table structure for table `accounts_bank`
--

DROP TABLE IF EXISTS `accounts_bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assets` decimal(15,4) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `rate` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_bank`
--

/*!40000 ALTER TABLE `accounts_bank` DISABLE KEYS */;
INSERT INTO `accounts_bank` VALUES (1,10000.0000,'','','',0.0000);
/*!40000 ALTER TABLE `accounts_bank` ENABLE KEYS */;

--
-- Table structure for table `accounts_bank_financial_reports`
--

DROP TABLE IF EXISTS `accounts_bank_financial_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_bank_financial_reports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_id` int(11) NOT NULL,
  `privatefile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bank_id` (`bank_id`,`privatefile_id`),
  KEY `accounts_bank_financial_reports_df49f419` (`bank_id`),
  KEY `accounts_bank_financial_reports_51d6352d` (`privatefile_id`),
  CONSTRAINT `bank_id_refs_id_f8d364b0` FOREIGN KEY (`bank_id`) REFERENCES `accounts_bank` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_bank_financial_reports`
--

/*!40000 ALTER TABLE `accounts_bank_financial_reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_bank_financial_reports` ENABLE KEYS */;

--
-- Table structure for table `accounts_company`
--

DROP TABLE IF EXISTS `accounts_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assets` decimal(15,4) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `industry_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_company_c3dc70a9` (`industry_id`),
  CONSTRAINT `industry_id_refs_id_fcf77e62` FOREIGN KEY (`industry_id`) REFERENCES `accounts_industry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_company`
--

/*!40000 ALTER TABLE `accounts_company` DISABLE KEYS */;
INSERT INTO `accounts_company` VALUES (1,0.0000,'company','','',1);
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
-- Table structure for table `accounts_fund`
--

DROP TABLE IF EXISTS `accounts_fund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_fund` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assets` decimal(15,4) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_fund`
--

/*!40000 ALTER TABLE `accounts_fund` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_fund` ENABLE KEYS */;

--
-- Table structure for table `accounts_fundcompany`
--

DROP TABLE IF EXISTS `accounts_fundcompany`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_fundcompany` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assets` decimal(15,4) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `contact` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_fundcompany`
--

/*!40000 ALTER TABLE `accounts_fundcompany` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_fundcompany` ENABLE KEYS */;

--
-- Table structure for table `accounts_fundcompany_financial_reports`
--

DROP TABLE IF EXISTS `accounts_fundcompany_financial_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_fundcompany_financial_reports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fundcompany_id` int(11) NOT NULL,
  `privatefile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fundcompany_id` (`fundcompany_id`,`privatefile_id`),
  KEY `accounts_fundcompany_financial_reports_a6ac429c` (`fundcompany_id`),
  KEY `accounts_fundcompany_financial_reports_51d6352d` (`privatefile_id`),
  CONSTRAINT `fundcompany_id_refs_id_76383c1b` FOREIGN KEY (`fundcompany_id`) REFERENCES `accounts_fundcompany` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_fundcompany_financial_reports`
--

/*!40000 ALTER TABLE `accounts_fundcompany_financial_reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_fundcompany_financial_reports` ENABLE KEYS */;

--
-- Table structure for table `accounts_government`
--

DROP TABLE IF EXISTS `accounts_government`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_government` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assets` decimal(15,4) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `position` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_government`
--

/*!40000 ALTER TABLE `accounts_government` DISABLE KEYS */;
INSERT INTO `accounts_government` VALUES (1,10000.0000,'政府','M','');
/*!40000 ALTER TABLE `accounts_government` ENABLE KEYS */;

--
-- Table structure for table `accounts_industry`
--

DROP TABLE IF EXISTS `accounts_industry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_industry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `section_id` int(11) NOT NULL,
  `display_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_industry_b402b60b` (`section_id`),
  CONSTRAINT `section_id_refs_id_562bbf6e` FOREIGN KEY (`section_id`) REFERENCES `accounts_section` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_industry`
--

/*!40000 ALTER TABLE `accounts_industry` DISABLE KEYS */;
INSERT INTO `accounts_industry` VALUES (1,1,'B');
/*!40000 ALTER TABLE `accounts_industry` ENABLE KEYS */;

--
-- Table structure for table `accounts_media`
--

DROP TABLE IF EXISTS `accounts_media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(50) NOT NULL,
  `contact` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_media`
--

/*!40000 ALTER TABLE `accounts_media` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_media` ENABLE KEYS */;

--
-- Table structure for table `accounts_person`
--

DROP TABLE IF EXISTS `accounts_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assets` decimal(15,4) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `position` varchar(20) NOT NULL,
  `company_type_id` int(11) DEFAULT NULL,
  `company_object_id` int(10) unsigned DEFAULT NULL,
  `industry_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_person_a3c9d75e` (`company_type_id`),
  KEY `accounts_person_c3dc70a9` (`industry_id`),
  CONSTRAINT `company_type_id_refs_id_2a440fb2` FOREIGN KEY (`company_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `industry_id_refs_id_e5ce6093` FOREIGN KEY (`industry_id`) REFERENCES `accounts_industry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_person`
--

/*!40000 ALTER TABLE `accounts_person` DISABLE KEYS */;
INSERT INTO `accounts_person` VALUES (1,10000.0000,'','M','',13,1,1),(2,10000.0000,'test2','M','',13,1,1);
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
-- Table structure for table `accounts_section`
--

DROP TABLE IF EXISTS `accounts_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_section`
--

/*!40000 ALTER TABLE `accounts_section` DISABLE KEYS */;
INSERT INTO `accounts_section` VALUES (1,'A');
/*!40000 ALTER TABLE `accounts_section` ENABLE KEYS */;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile`
--

/*!40000 ALTER TABLE `accounts_userprofile` DISABLE KEYS */;
INSERT INTO `accounts_userprofile` VALUES (1,2,13,1),(2,3,11,1),(3,4,11,2),(4,5,15,1),(5,6,12,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'writer');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,52);
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
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add log entry',6,'add_logentry'),(17,'Can change log entry',6,'change_logentry'),(18,'Can delete log entry',6,'delete_logentry'),(19,'Can add user profile',7,'add_userprofile'),(20,'Can change user profile',7,'change_userprofile'),(21,'Can delete user profile',7,'delete_userprofile'),(22,'Can add media',8,'add_media'),(23,'Can change media',8,'change_media'),(24,'Can delete media',8,'delete_media'),(25,'Can add section',9,'add_section'),(26,'Can change section',9,'change_section'),(27,'Can delete section',9,'delete_section'),(28,'Can add industry',10,'add_industry'),(29,'Can change industry',10,'change_industry'),(30,'Can delete industry',10,'delete_industry'),(31,'Can add person',11,'add_person'),(32,'Can change person',11,'change_person'),(33,'Can delete person',11,'delete_person'),(34,'Can add government',12,'add_government'),(35,'Can change government',12,'change_government'),(36,'Can delete government',12,'delete_government'),(37,'Can add company',13,'add_company'),(38,'Can change company',13,'change_company'),(39,'Can delete company',13,'delete_company'),(40,'Can add fund company',14,'add_fundcompany'),(41,'Can change fund company',14,'change_fundcompany'),(42,'Can delete fund company',14,'delete_fundcompany'),(43,'Can add bank',15,'add_bank'),(44,'Can change bank',15,'change_bank'),(45,'Can delete bank',15,'delete_bank'),(46,'Can add fund',16,'add_fund'),(47,'Can change fund',16,'change_fund'),(48,'Can delete fund',16,'delete_fund'),(49,'Can add passage',17,'add_passage'),(50,'Can change passage',17,'change_passage'),(51,'Can delete passage',17,'delete_passage'),(52,'Publish passage.',17,'publish_passage'),(53,'Can add comment',18,'add_comment'),(54,'Can change comment',18,'change_comment'),(55,'Can delete comment',18,'delete_comment'),(56,'Can add file',19,'add_file'),(57,'Can change file',19,'change_file'),(58,'Can delete file',19,'delete_file'),(59,'Can add public file',19,'add_publicfile'),(60,'Can change public file',19,'change_publicfile'),(61,'Can delete public file',19,'delete_publicfile'),(62,'Can add private file',19,'add_privatefile'),(63,'Can change private file',19,'change_privatefile'),(64,'Can delete private file',19,'delete_privatefile'),(65,'Can add fund',22,'add_fund'),(66,'Can change fund',22,'change_fund'),(67,'Can delete fund',22,'delete_fund'),(68,'Can add ransom application',23,'add_ransomapplication'),(69,'Can change ransom application',23,'change_ransomapplication'),(70,'Can delete ransom application',23,'delete_ransomapplication'),(71,'Can add share',24,'add_share'),(72,'Can change share',24,'change_share'),(73,'Can delete share',24,'delete_share'),(74,'Can add stock',25,'add_stock'),(75,'Can change stock',25,'change_stock'),(76,'Can delete stock',25,'delete_stock'),(77,'Can add log',26,'add_log'),(78,'Can change log',26,'change_log'),(79,'Can delete log',26,'delete_log'),(80,'Can add application',27,'add_application'),(81,'Can change application',27,'change_application'),(82,'Can delete application',27,'delete_application'),(83,'Can add share',28,'add_share'),(84,'Can change share',28,'change_share'),(85,'Can delete share',28,'delete_share'),(86,'Can add future',29,'add_future'),(87,'Can change future',29,'change_future'),(88,'Can delete future',29,'delete_future'),(89,'Can add bond',30,'add_bond'),(90,'Can change bond',30,'change_bond'),(91,'Can delete bond',30,'delete_bond'),(92,'Can add share',31,'add_share'),(93,'Can change share',31,'change_share'),(94,'Can delete share',31,'delete_share'),(95,'Can add notification',32,'add_notification'),(96,'Can change notification',32,'change_notification'),(97,'Can delete notification',32,'delete_notification'),(98,'Can add deposit',33,'add_deposit'),(99,'Can change deposit',33,'change_deposit'),(100,'Can delete deposit',33,'delete_deposit'),(101,'Can add transfer log',34,'add_transferlog'),(102,'Can change transfer log',34,'change_transferlog'),(103,'Can delete transfer log',34,'delete_transferlog');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$qVPV2uXAEimE$k+RLz6EiFT66M18IfwtyPiR0FV0Oig7z0Cj4bZoZ5Do=','2014-06-15 14:44:53',1,'superuser','','','',1,1,'2014-06-15 14:44:53'),(2,'pbkdf2_sha256$10000$7O39jMbbWuGi$iQvff2mlfUNoPh8IHOytEZy8oriSbFQdJkxHGZmHK14=','2014-06-15 14:46:08',0,'cpy','','','',0,1,'2014-06-15 14:46:08'),(3,'pbkdf2_sha256$10000$K6PVyyE98DWU$h2x8N0z7Ry3/BmtJ8dOg+mNcCUElPfSpxGsLFK1h5us=','2014-06-15 14:46:08',0,'test','','','',0,1,'2014-06-15 14:46:08'),(4,'pbkdf2_sha256$10000$uHGL1lhu0UU2$NUtCPWyVhhqhtwM86ZyiZdkQX0sl3Z9lz3HroSMWsgs=','2014-06-15 14:46:09',0,'test2','','','',0,1,'2014-06-15 14:46:09'),(5,'pbkdf2_sha256$10000$ARo0WSjOu33l$Kg5YCjb2ClwWzhiHEq8DgxeBytf1t8MjmVv+WPM1v0s=','2014-06-15 14:46:09',0,'bank','','','',0,1,'2014-06-15 14:46:09'),(6,'pbkdf2_sha256$10000$FffayfTHyIV8$DQI6F3RPbEDYoR9P2d6/W7zQ50HqgoQff8Mhobkdy8A=','2014-06-15 14:46:09',0,'zf','','','',0,1,'2014-06-15 14:46:09');
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
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1),(2,5,1),(3,6,1);
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
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
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
  `display_name` varchar(255) NOT NULL,
  `publisher_type_id` int(11) DEFAULT NULL,
  `publisher_object_id` int(10) unsigned DEFAULT NULL,
  `type` varchar(3) NOT NULL,
  `published` tinyint(1) NOT NULL,
  `profit_rate` decimal(15,4) NOT NULL,
  `lasted_time` int(10) unsigned NOT NULL,
  `published_time` datetime NOT NULL,
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bonds_bond_e552aa7d` (`publisher_type_id`),
  CONSTRAINT `publisher_type_id_refs_id_e5ac30fb` FOREIGN KEY (`publisher_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bonds_bond`
--

/*!40000 ALTER TABLE `bonds_bond` DISABLE KEYS */;
/*!40000 ALTER TABLE `bonds_bond` ENABLE KEYS */;

--
-- Table structure for table `bonds_share`
--

DROP TABLE IF EXISTS `bonds_share`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bonds_share` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_type_id` int(11) DEFAULT NULL,
  `owner_object_id` int(10) unsigned DEFAULT NULL,
  `bond_id` int(11) NOT NULL,
  `money` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bonds_share_c7a7a7fc` (`owner_type_id`),
  KEY `bonds_share_9da191f0` (`bond_id`),
  CONSTRAINT `owner_type_id_refs_id_f348ff08` FOREIGN KEY (`owner_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `bond_id_refs_id_46d8f579` FOREIGN KEY (`bond_id`) REFERENCES `bonds_bond` (`id`)
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
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'log entry','admin','logentry'),(7,'user profile','accounts','userprofile'),(8,'media','accounts','media'),(9,'section','accounts','section'),(10,'industry','accounts','industry'),(11,'person','accounts','person'),(12,'government','accounts','government'),(13,'company','accounts','company'),(14,'fund company','accounts','fundcompany'),(15,'bank','accounts','bank'),(16,'fund','accounts','fund'),(17,'passage','webboard','passage'),(18,'comment','webboard','comment'),(19,'file','files','file'),(20,'private file','files','privatefile'),(21,'public file','files','publicfile'),(22,'fund','funds','fund'),(23,'ransom application','funds','ransomapplication'),(24,'share','funds','share'),(25,'stock','stocks','stock'),(26,'log','stocks','log'),(27,'application','stocks','application'),(28,'share','stocks','share'),(29,'future','futures','future'),(30,'bond','bonds','bond'),(31,'share','bonds','share'),(32,'notification','notifications','notification'),(33,'deposit','transfer','deposit'),(34,'transfer log','transfer','transferlog');
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
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

--
-- Table structure for table `files_file`
--

DROP TABLE IF EXISTS `files_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `files_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` datetime NOT NULL,
  `file` varchar(100) NOT NULL,
  `file_type` varchar(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files_file`
--

/*!40000 ALTER TABLE `files_file` DISABLE KEYS */;
/*!40000 ALTER TABLE `files_file` ENABLE KEYS */;

--
-- Table structure for table `funds_fund`
--

DROP TABLE IF EXISTS `funds_fund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funds_fund` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(255) NOT NULL,
  `publisher_type_id` int(11) DEFAULT NULL,
  `publisher_object_id` int(10) unsigned DEFAULT NULL,
  `account_id` int(11) DEFAULT NULL,
  `published` tinyint(1) NOT NULL,
  `min_return_rate` decimal(15,4) NOT NULL,
  `return_rate` decimal(15,4) NOT NULL,
  `max_return_rate` decimal(15,4) NOT NULL,
  `initial_money` decimal(15,4) NOT NULL,
  `lasted_time` int(10) unsigned NOT NULL,
  `published_time` datetime NOT NULL,
  `fund_type` varchar(10) NOT NULL,
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_id` (`account_id`),
  KEY `funds_fund_e552aa7d` (`publisher_type_id`),
  CONSTRAINT `publisher_type_id_refs_id_5f61e5eb` FOREIGN KEY (`publisher_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `account_id_refs_id_3fe423da` FOREIGN KEY (`account_id`) REFERENCES `accounts_fund` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funds_fund`
--

/*!40000 ALTER TABLE `funds_fund` DISABLE KEYS */;
/*!40000 ALTER TABLE `funds_fund` ENABLE KEYS */;

--
-- Table structure for table `funds_ransomapplication`
--

DROP TABLE IF EXISTS `funds_ransomapplication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funds_ransomapplication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fund_id` int(11) NOT NULL,
  `owner_type_id` int(11) DEFAULT NULL,
  `owner_object_id` int(10) unsigned DEFAULT NULL,
  `money` decimal(15,4) NOT NULL,
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `funds_ransomapplication_5ca8288d` (`fund_id`),
  KEY `funds_ransomapplication_c7a7a7fc` (`owner_type_id`),
  CONSTRAINT `owner_type_id_refs_id_37197dad` FOREIGN KEY (`owner_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `fund_id_refs_id_6e486aad` FOREIGN KEY (`fund_id`) REFERENCES `funds_fund` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funds_ransomapplication`
--

/*!40000 ALTER TABLE `funds_ransomapplication` DISABLE KEYS */;
/*!40000 ALTER TABLE `funds_ransomapplication` ENABLE KEYS */;

--
-- Table structure for table `funds_share`
--

DROP TABLE IF EXISTS `funds_share`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funds_share` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_type_id` int(11) DEFAULT NULL,
  `owner_object_id` int(10) unsigned DEFAULT NULL,
  `fund_id` int(11) NOT NULL,
  `money` decimal(15,4) NOT NULL,
  `percentage` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `funds_share_c7a7a7fc` (`owner_type_id`),
  KEY `funds_share_5ca8288d` (`fund_id`),
  CONSTRAINT `owner_type_id_refs_id_f6993360` FOREIGN KEY (`owner_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `fund_id_refs_id_5045f3de` FOREIGN KEY (`fund_id`) REFERENCES `funds_fund` (`id`)
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
  `display_name` varchar(30) NOT NULL,
  `current_price` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `futures_future`
--

/*!40000 ALTER TABLE `futures_future` DISABLE KEYS */;
/*!40000 ALTER TABLE `futures_future` ENABLE KEYS */;

--
-- Table structure for table `notifications_notification`
--

DROP TABLE IF EXISTS `notifications_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notifications_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recipient_id` int(11) NOT NULL,
  `unread` tinyint(1) NOT NULL,
  `confirmed` tinyint(1) NOT NULL,
  `actor_text` varchar(255) DEFAULT NULL,
  `actor_content_type_id` int(11) DEFAULT NULL,
  `actor_object_id` varchar(255) DEFAULT NULL,
  `verb` varchar(255) NOT NULL,
  `target_text` varchar(255) DEFAULT NULL,
  `target_content_type_id` int(11) DEFAULT NULL,
  `target_object_id` varchar(255) DEFAULT NULL,
  `created_time` datetime NOT NULL,
  `message` longtext NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `action` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `notifications_notification_3e31d986` (`recipient_id`),
  KEY `notifications_notification_3df58830` (`actor_content_type_id`),
  KEY `notifications_notification_276d0c93` (`target_content_type_id`),
  CONSTRAINT `target_content_type_id_refs_id_a9511998` FOREIGN KEY (`target_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `actor_content_type_id_refs_id_a9511998` FOREIGN KEY (`actor_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `recipient_id_refs_id_cab99939` FOREIGN KEY (`recipient_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications_notification`
--

/*!40000 ALTER TABLE `notifications_notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `notifications_notification` ENABLE KEYS */;

--
-- Table structure for table `stocks_application`
--

DROP TABLE IF EXISTS `stocks_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stocks_application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `applicant_type_id` int(11) DEFAULT NULL,
  `applicant_object_id` int(10) unsigned DEFAULT NULL,
  `stock_id` int(11) NOT NULL,
  `command` varchar(4) NOT NULL,
  `price` decimal(15,4) NOT NULL,
  `shares` decimal(15,4) NOT NULL,
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stocks_application_bf5325b1` (`applicant_type_id`),
  KEY `stocks_application_80945c99` (`stock_id`),
  CONSTRAINT `applicant_type_id_refs_id_bcd93f28` FOREIGN KEY (`applicant_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `stock_id_refs_id_f6a97a14` FOREIGN KEY (`stock_id`) REFERENCES `stocks_stock` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks_application`
--

/*!40000 ALTER TABLE `stocks_application` DISABLE KEYS */;
/*!40000 ALTER TABLE `stocks_application` ENABLE KEYS */;

--
-- Table structure for table `stocks_log`
--

DROP TABLE IF EXISTS `stocks_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stocks_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_id` int(11) NOT NULL,
  `price` decimal(15,4) NOT NULL,
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stocks_log_80945c99` (`stock_id`),
  CONSTRAINT `stock_id_refs_id_e02f135a` FOREIGN KEY (`stock_id`) REFERENCES `stocks_stock` (`id`)
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
  `owner_type_id` int(11) DEFAULT NULL,
  `owner_object_id` int(10) unsigned DEFAULT NULL,
  `stock_id` int(11) NOT NULL,
  `shares` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stocks_share_c7a7a7fc` (`owner_type_id`),
  KEY `stocks_share_80945c99` (`stock_id`),
  CONSTRAINT `owner_type_id_refs_id_b2069a99` FOREIGN KEY (`owner_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `stock_id_refs_id_14b2e948` FOREIGN KEY (`stock_id`) REFERENCES `stocks_stock` (`id`)
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
  `display_name` varchar(255) NOT NULL,
  `publisher_type_id` int(11) DEFAULT NULL,
  `publisher_object_id` int(10) unsigned DEFAULT NULL,
  `current_price` decimal(15,4) NOT NULL,
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stocks_stock_e552aa7d` (`publisher_type_id`),
  CONSTRAINT `publisher_type_id_refs_id_e629e857` FOREIGN KEY (`publisher_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks_stock`
--

/*!40000 ALTER TABLE `stocks_stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `stocks_stock` ENABLE KEYS */;

--
-- Table structure for table `transfer_deposit`
--

DROP TABLE IF EXISTS `transfer_deposit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transfer_deposit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_id` int(11) NOT NULL,
  `owner_content_type_id` int(11) NOT NULL,
  `owner_object_id` varchar(255) NOT NULL,
  `money` decimal(15,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transfer_deposit_df49f419` (`bank_id`),
  KEY `transfer_deposit_f49a921f` (`owner_content_type_id`),
  CONSTRAINT `owner_content_type_id_refs_id_36598671` FOREIGN KEY (`owner_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `bank_id_refs_id_d9c798fa` FOREIGN KEY (`bank_id`) REFERENCES `accounts_bank` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transfer_deposit`
--

/*!40000 ALTER TABLE `transfer_deposit` DISABLE KEYS */;
/*!40000 ALTER TABLE `transfer_deposit` ENABLE KEYS */;

--
-- Table structure for table `transfer_transferlog`
--

DROP TABLE IF EXISTS `transfer_transferlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transfer_transferlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `transfer_by_content_type_id` int(11) NOT NULL,
  `transfer_by_object_id` varchar(255) NOT NULL,
  `transfer_to_content_type_id` int(11) NOT NULL,
  `transfer_to_object_id` varchar(255) NOT NULL,
  `money` decimal(15,4) NOT NULL,
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transfer_transferlog_1c89a19b` (`transfer_by_content_type_id`),
  KEY `transfer_transferlog_9a243791` (`transfer_to_content_type_id`),
  CONSTRAINT `transfer_to_content_type_id_refs_id_5d7d7048` FOREIGN KEY (`transfer_to_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `transfer_by_content_type_id_refs_id_5d7d7048` FOREIGN KEY (`transfer_by_content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transfer_transferlog`
--

/*!40000 ALTER TABLE `transfer_transferlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `transfer_transferlog` ENABLE KEYS */;

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
  PRIMARY KEY (`id`),
  KEY `webboard_comment_e969df21` (`author_id`),
  KEY `webboard_comment_e215af53` (`passage_id`),
  CONSTRAINT `author_id_refs_id_6e715fa5` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `passage_id_refs_id_a7611baa` FOREIGN KEY (`passage_id`) REFERENCES `webboard_passage` (`id`)
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
  KEY `webboard_passage_e969df21` (`author_id`),
  CONSTRAINT `author_id_refs_id_d4b3e522` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webboard_passage`
--

/*!40000 ALTER TABLE `webboard_passage` DISABLE KEYS */;
/*!40000 ALTER TABLE `webboard_passage` ENABLE KEYS */;

--
-- Table structure for table `webboard_passage_attachments`
--

DROP TABLE IF EXISTS `webboard_passage_attachments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webboard_passage_attachments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `passage_id` int(11) NOT NULL,
  `publicfile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `passage_id` (`passage_id`,`publicfile_id`),
  KEY `webboard_passage_attachments_e215af53` (`passage_id`),
  KEY `webboard_passage_attachments_1b5b81cb` (`publicfile_id`),
  CONSTRAINT `passage_id_refs_id_c4a6663f` FOREIGN KEY (`passage_id`) REFERENCES `webboard_passage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webboard_passage_attachments`
--

/*!40000 ALTER TABLE `webboard_passage_attachments` DISABLE KEYS */;
/*!40000 ALTER TABLE `webboard_passage_attachments` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-06-15 14:46:48
