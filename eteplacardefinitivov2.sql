CREATE DATABASE  IF NOT EXISTS `etemfl83_inter_classe` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `etemfl83_inter_classe`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: etemfl83_inter_classe
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `pk_matricula` int NOT NULL,
  `nome_aluno` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_nome_turma` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_classificacao` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`pk_matricula`),
  KEY `fk_nome_turma` (`fk_nome_turma`),
  CONSTRAINT `alunos_ibfk_1` FOREIGN KEY (`fk_nome_turma`) REFERENCES `turmas` (`pk_nome_turma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (1,'Maria Eduarda','3TDSB','Feminino'),(2,'Ana Paula','3TDSA','Feminino'),(3,'Juliana Costa','3MKTA','Feminino'),(4,'Camila Rocha','3MKTB','Feminino'),(5,'Oziel da Silva','3TDSB','Masculino'),(6,'Guilherme Henrique','3TDSB','Masculino'),(7,'Luis Henrique','3TDSB','Masculino'),(8,'João Pedro','3TDSA','Masculino'),(9,'Mateus Almeida','3TDSA','Masculino'),(10,'Felipe Barbosa','3TDSA','Masculino'),(11,'André Santos','3MKTA','Masculino'),(12,'Thiago Ferreira','3MKTA','Masculino'),(13,'Vinícius Oliveira','3MKTA','Masculino'),(14,'Bruno Carvalho','3MKTB','Masculino'),(15,'Pedro Henrique','3MKTB','Masculino'),(16,'Caio Martins','3MKTB','Masculino'),(23,'Giovanna ','1TDSB','Feminino'),(333,'Ryan Lucas','3TDSB','Masculino'),(10000000,'Matheus Oliveira','3TDSB','Masculino'),(10000003,'Clara','3MKTB','Feminino'),(10000004,'Maria','3TDSB','Feminino'),(10000005,'Ana','3TDSB','Feminino'),(10000006,'joao','3MKTB','Masculino'),(12345559,'pedro vitor','3TDSB','Masculino'),(98761234,'Soraya Morgana','3MKTB','Feminino');
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calendario`
--

DROP TABLE IF EXISTS `calendario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calendario` (
  `pk_evento` int NOT NULL AUTO_INCREMENT,
  `dia_evento` date DEFAULT NULL,
  `fk_partida` int DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fim` time DEFAULT NULL,
  PRIMARY KEY (`pk_evento`),
  KEY `fk_partida` (`fk_partida`),
  CONSTRAINT `calendario_ibfk_1` FOREIGN KEY (`fk_partida`) REFERENCES `partidas` (`pk_partida`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendario`
--

LOCK TABLES `calendario` WRITE;
/*!40000 ALTER TABLE `calendario` DISABLE KEYS */;
INSERT INTO `calendario` VALUES (1,'2025-10-07',67,NULL,NULL),(4,'2025-10-07',70,NULL,NULL),(5,'2025-10-07',71,NULL,NULL),(6,'2025-10-07',72,NULL,NULL),(8,'2025-10-03',74,NULL,NULL),(11,'2025-10-03',77,NULL,NULL),(12,'2025-10-07',78,NULL,NULL),(13,'2025-10-03',79,NULL,NULL),(14,'2025-10-07',80,NULL,NULL),(15,'2025-10-07',81,NULL,NULL),(16,'2025-10-07',82,NULL,NULL),(18,'2025-10-07',84,NULL,NULL);
/*!40000 ALTER TABLE `calendario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classificacao`
--

DROP TABLE IF EXISTS `classificacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classificacao` (
  `pk_descricao` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`pk_descricao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classificacao`
--

LOCK TABLES `classificacao` WRITE;
/*!40000 ALTER TABLE `classificacao` DISABLE KEYS */;
INSERT INTO `classificacao` VALUES ('Feminino'),('Masculino'),('Misto');
/*!40000 ALTER TABLE `classificacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipes`
--

DROP TABLE IF EXISTS `equipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipes` (
  `pk_equipe` int NOT NULL AUTO_INCREMENT,
  `fk_esporte` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_nome_turma` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_descricao` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `nome_equipe` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`pk_equipe`),
  KEY `fk_esporte` (`fk_esporte`),
  KEY `fk_nome_turma` (`fk_nome_turma`),
  KEY `fk_descricao` (`fk_descricao`),
  CONSTRAINT `equipes_ibfk_1` FOREIGN KEY (`fk_esporte`) REFERENCES `esportes` (`pk_esporte`),
  CONSTRAINT `equipes_ibfk_2` FOREIGN KEY (`fk_nome_turma`) REFERENCES `turmas` (`pk_nome_turma`),
  CONSTRAINT `equipes_ibfk_3` FOREIGN KEY (`fk_descricao`) REFERENCES `classificacao` (`pk_descricao`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipes`
--

LOCK TABLES `equipes` WRITE;
/*!40000 ALTER TABLE `equipes` DISABLE KEYS */;
INSERT INTO `equipes` VALUES (18,'Futsal','3TDSB','Masculino','A'),(21,'Basquete','3TDSB','Feminino','A'),(22,'Queimada','3TDSB','Misto','B'),(23,'Queimada','3TDSB','Misto','A'),(25,'Tênis de Mesa','3TDSB','Feminino','A'),(26,'Tênis de Mesa','3TDSB','Masculino','B'),(27,'Futsal','3TDSA','Masculino','A'),(28,'Basquete','3TDSA','Feminino','A'),(29,'Queimada','3TDSA','Misto','A'),(30,'Queimada','3TDSA','Misto','B'),(32,'Tênis de Mesa','3TDSA','Feminino','A'),(33,'Tênis de Mesa','3TDSA','Masculino','B'),(34,'Futsal','3MKTA','Masculino','A'),(35,'Basquete','3MKTA','Feminino','A'),(36,'Queimada','3MKTA','Misto','A'),(37,'Queimada','3MKTA','Misto','B'),(39,'Tênis de Mesa','3MKTA','Feminino','A'),(40,'Tênis de Mesa','3MKTA','Masculino','B'),(41,'Futsal','3MKTB','Masculino','A'),(42,'Basquete','3MKTB','Feminino','A'),(43,'Queimada','3MKTB','Misto','A'),(44,'Queimada','3MKTB','Misto','B'),(46,'Tênis de Mesa','3MKTB','Feminino','A'),(47,'Tênis de Mesa','3MKTB','Masculino','B'),(48,'Xadrez','3TDSB','Masculino','A'),(49,'Xadrez','3TDSA','Masculino','A'),(50,'Xadrez','3TDSB','Masculino','B'),(51,'Futsal','3TDSB','Masculino','B');
/*!40000 ALTER TABLE `equipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `esportes`
--

DROP TABLE IF EXISTS `esportes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `esportes` (
  `pk_esporte` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `grupo` enum('Coletivo','Individual') CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `qtd_jogadores` int NOT NULL,
  PRIMARY KEY (`pk_esporte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `esportes`
--

LOCK TABLES `esportes` WRITE;
/*!40000 ALTER TABLE `esportes` DISABLE KEYS */;
INSERT INTO `esportes` VALUES ('Basquete','Coletivo',8),('Futsal','Coletivo',8),('Handebol','Coletivo',8),('Queimada','Coletivo',8),('Tênis de Mesa','Individual',1),('Vôlei','Coletivo',6),('Xadrez','Individual',1);
/*!40000 ALTER TABLE `esportes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estatisticas_esporte`
--

DROP TABLE IF EXISTS `estatisticas_esporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estatisticas_esporte` (
  `fk_esporte` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `fk_nome_estatistica` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`fk_esporte`,`fk_nome_estatistica`),
  KEY `fk_nome_estatistica` (`fk_nome_estatistica`),
  CONSTRAINT `estatisticas_esporte_ibfk_1` FOREIGN KEY (`fk_esporte`) REFERENCES `esportes` (`pk_esporte`),
  CONSTRAINT `estatisticas_esporte_ibfk_2` FOREIGN KEY (`fk_nome_estatistica`) REFERENCES `tipo_estatistica` (`pk_nome_estatistica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estatisticas_esporte`
--

LOCK TABLES `estatisticas_esporte` WRITE;
/*!40000 ALTER TABLE `estatisticas_esporte` DISABLE KEYS */;
INSERT INTO `estatisticas_esporte` VALUES ('Basquete','Arremessos de Três'),('Queimada','Eliminações'),('Futsal','Finalizações'),('Futsal','Gols'),('Basquete','Passes'),('Futsal','Passes'),('Basquete','Pontos'),('Tênis de Mesa','Sets'),('Xadrez','Sets');
/*!40000 ALTER TABLE `estatisticas_esporte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estatisticas_partida`
--

DROP TABLE IF EXISTS `estatisticas_partida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estatisticas_partida` (
  `fk_partida` int NOT NULL,
  `fk_nome_estatistica` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `valor_time_casa` int DEFAULT NULL,
  `valor_time_visitante` int DEFAULT NULL,
  PRIMARY KEY (`fk_partida`,`fk_nome_estatistica`),
  KEY `fk_nome_estatistica` (`fk_nome_estatistica`),
  CONSTRAINT `estatisticas_partida_ibfk_1` FOREIGN KEY (`fk_partida`) REFERENCES `partidas` (`pk_partida`),
  CONSTRAINT `estatisticas_partida_ibfk_2` FOREIGN KEY (`fk_nome_estatistica`) REFERENCES `tipo_estatistica` (`pk_nome_estatistica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estatisticas_partida`
--

LOCK TABLES `estatisticas_partida` WRITE;
/*!40000 ALTER TABLE `estatisticas_partida` DISABLE KEYS */;
INSERT INTO `estatisticas_partida` VALUES (67,'Finalizações',7,10),(67,'Gols',7,1),(67,'Passes',1,51),(70,'Arremessos de Três',0,0),(70,'Passes',0,0),(70,'Pontos',1,0),(71,'Eliminações',1,0),(72,'Eliminações',0,0),(74,'Eliminações',0,0),(77,'Sets',0,0),(78,'Sets',3,2),(79,'Sets',0,0),(80,'Sets',1,0),(81,'Sets',4,0),(82,'Sets',0,0),(84,'Finalizações',1,0),(84,'Gols',2,2),(84,'Passes',1,0);
/*!40000 ALTER TABLE `estatisticas_partida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `pk_usuario` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `senha` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `nivel` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_nome_turma` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`pk_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('adm','adm','Administrador',NULL),('gio@gmail.com','212121','AlunoMonitor','1MKTB'),('Pinheiro','123456','Administrador',NULL),('ryan','123','AlunoMonitor','3TDSB'),('teste6','6666666','Administrador',NULL),('testeMetodo','100002','AlunoMonitor','1TDSB');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membros_equipe`
--

DROP TABLE IF EXISTS `membros_equipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membros_equipe` (
  `fk_equipe` int NOT NULL,
  `fk_matricula` int NOT NULL,
  PRIMARY KEY (`fk_equipe`,`fk_matricula`),
  KEY `fk_matricula` (`fk_matricula`),
  CONSTRAINT `membros_equipe_ibfk_1` FOREIGN KEY (`fk_equipe`) REFERENCES `equipes` (`pk_equipe`),
  CONSTRAINT `membros_equipe_ibfk_2` FOREIGN KEY (`fk_matricula`) REFERENCES `alunos` (`pk_matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membros_equipe`
--

LOCK TABLES `membros_equipe` WRITE;
/*!40000 ALTER TABLE `membros_equipe` DISABLE KEYS */;
INSERT INTO `membros_equipe` VALUES (25,1),(32,2),(39,3),(46,4),(48,5),(26,6),(50,6),(49,8),(33,9),(40,12),(47,15);
/*!40000 ALTER TABLE `membros_equipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partidas`
--

DROP TABLE IF EXISTS `partidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partidas` (
  `pk_partida` int NOT NULL AUTO_INCREMENT,
  `fk_esporte` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_descricao` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `fk_equipe_casa` int DEFAULT NULL,
  `fk_equipe_visitante` int DEFAULT NULL,
  `pontos_turma_casa` int DEFAULT NULL,
  `pontos_turma_visitante` int DEFAULT NULL,
  PRIMARY KEY (`pk_partida`),
  KEY `fk_esporte` (`fk_esporte`),
  KEY `fk_descricao` (`fk_descricao`),
  KEY `equipe_partidasfk_idx` (`fk_equipe_casa`),
  KEY `equipe_partidasfk2_idx` (`fk_equipe_visitante`),
  CONSTRAINT `equipe_partidasfk` FOREIGN KEY (`fk_equipe_casa`) REFERENCES `equipes` (`pk_equipe`),
  CONSTRAINT `equipe_partidasfk2` FOREIGN KEY (`fk_equipe_visitante`) REFERENCES `equipes` (`pk_equipe`),
  CONSTRAINT `partidas_ibfk_1` FOREIGN KEY (`fk_esporte`) REFERENCES `esportes` (`pk_esporte`),
  CONSTRAINT `partidas_ibfk_2` FOREIGN KEY (`fk_descricao`) REFERENCES `classificacao` (`pk_descricao`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partidas`
--

LOCK TABLES `partidas` WRITE;
/*!40000 ALTER TABLE `partidas` DISABLE KEYS */;
INSERT INTO `partidas` VALUES (67,'Futsal','Masculino',18,27,7,1),(70,'Basquete','Feminino',28,42,1,0),(71,'Queimada','Misto',22,29,1,0),(72,'Queimada','Misto',23,30,0,0),(74,'Queimada','Misto',37,44,0,0),(77,'Tênis de Mesa','Feminino',25,39,0,0),(78,'Tênis de Mesa','Feminino',32,46,3,2),(79,'Tênis de Mesa','Masculino',26,40,0,0),(80,'Tênis de Mesa','Masculino',33,47,1,0),(81,'Xadrez','Masculino',48,49,4,0),(82,'Xadrez','Masculino',48,50,0,0),(84,'Futsal','Masculino',18,51,2,2);
/*!40000 ALTER TABLE `partidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_estatistica`
--

DROP TABLE IF EXISTS `tipo_estatistica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_estatistica` (
  `pk_nome_estatistica` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`pk_nome_estatistica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_estatistica`
--

LOCK TABLES `tipo_estatistica` WRITE;
/*!40000 ALTER TABLE `tipo_estatistica` DISABLE KEYS */;
INSERT INTO `tipo_estatistica` VALUES ('Arremessos de Três'),('Eliminações'),('Empurrão'),('Empurrar'),('Finalizações'),('Fora Da Area'),('Gols'),('Matchpoints'),('Passes'),('Pontos'),('Rebotes'),('Saques'),('Sets');
/*!40000 ALTER TABLE `tipo_estatistica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turmas`
--

DROP TABLE IF EXISTS `turmas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turmas` (
  `pk_nome_turma` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `icone_url` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`pk_nome_turma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turmas`
--

LOCK TABLES `turmas` WRITE;
/*!40000 ALTER TABLE `turmas` DISABLE KEYS */;
INSERT INTO `turmas` VALUES ('1MKTA','/static/imgTurmas/1mkta.jpg'),('1MKTB','/static/imgTurmas/1mktb.jpg'),('1TDSA','/static/imgTurmas/1tdsa.jpg'),('1TDSB','/static/imgTurmas/1tdsb.jpg'),('2MKTA','/static/imgTurmas/2mkta.jpg'),('2MKTB','/static/imgTurmas/2mktb.jpg'),('2TDSA','/static/imgTurmas/2tdsa.jpg'),('2TDSB','/static/imgTurmas/2tdsb.jpg'),('3MKTA','/static/imgTurmas/3mkta.jpg'),('3MKTB','/static/imgTurmas/3mktb.jpg'),('3TDSA','/static/imgTurmas/3tdsa.jpg'),('3TDSB','/static/imgTurmas/3tdsb.jpg'),('TurmaTeste','/imag.png');
/*!40000 ALTER TABLE `turmas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-06 16:47:01
