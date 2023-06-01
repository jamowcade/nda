-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 22, 2023 at 06:04 AM
-- Server version: 8.0.33
-- PHP Version: 8.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_nda`
--

-- --------------------------------------------------------

--
-- Table structure for table `main_campany`
--

CREATE TABLE `main_campany` (
  `id` bigint NOT NULL,
  `title` varchar(50) NOT NULL,
  `owner` varchar(50) NOT NULL,
  `timestamp` date NOT NULL,
  `asn` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_campany`
--

INSERT INTO `main_campany` (`id`, `title`, `owner`, `timestamp`, `asn`) VALUES
(1, 'Telesom', 'Telesom', '2023-05-21', 'AS37473 '),
(2, 'Global Internet Company	', 'Global Internet Compay', '2023-05-21', 'AS37326'),
(3, ' Hormuud Telecom Somalia INC', ' Hormuud Telecom Somalia INC', '2023-05-21', 'AS37371'),
(4, 'Golis Telecom Somalia  ·  golis.net', 'Golis Telecom Somalia', '2023-05-21', 'AS328250'),
(5, 'SOMTEL INTERNATIONAL Ltd  ·  somtelnetwork.net', 'SOMTEL INTERNATIONAL Ltd', '2023-05-21', 'AS37563'),
(6, 'Economic & Strategic Research Center ', 'Economic & Strategic Research Center ', '2023-05-21', 'AS328435'),
(7, 'Somtel Somalia LTD  ·  somtelnetwork.net', 'Somtel Somalia LTD', '2023-05-21', 'AS328469'),
(8, 'SomCable  ·  somcable.com', ' SomCable', '2023-05-21', 'AS37425'),
(9, 'SomaliREN', ' Somali Research & Education Network(SomaliREN)', '2023-05-21', 'AS327764'),
(10, 'Somcast Networks LLC  ·  somcast.so', 'Somcast Networks LLC', '2023-05-21', 'AS327768'),
(11, 'Somali Optical Networks  ·  son.com.so', 'Somali Optical Networks', '2023-05-22', 'AS327828'),
(12, 'Sahal Telecom Somalia  ·  sahaltel.com', 'Sahal Telecom Somalia', '2023-05-22', 'AS327747'),
(13, 'Somlink Wireless Network  ·  somlink.net', 'Somlink Wireless Network', '2023-05-22', 'AS328590'),
(14, 'SO! Limited  ·  sogasho.com', 'SO! Limited', '2023-05-22', 'AS328959'),
(15, 'Somali Wireless Network  ·  somaliawireless.com', 'Somali Wireless Network', '2023-05-22', 'AS327742'),
(16, 'AMTEL LTD  ·  amtelkom.com', 'AMTEL LTD', '2023-05-22', 'AS328319'),
(17, 'Bluecom Ltd  ·  bluecom.so', 'Bluecom Ltd', '2023-05-22', 'AS328954'),
(18, 'TAYOCOM  ·  tayocom.com', 'TAYOCOM', '2023-05-22', 'AS328953'),
(19, 'mptt.gov.so', 'Ministry of Posts, T & T', '2023-05-22', 'AS37644'),
(20, 'Dalkom Somalia  ·  dalkomsomalia.com', 'Dalkom Somalia', '2023-05-22', 'AS329163'),
(21, 'SomaliREN  ·  nca.gov.so', 'Somali Research & Education Network', '2023-05-22', 'AS328363'),
(22, 'SomaliREN  nca.gov.so', 'Somali Research & Education Network', '2023-05-22', 'AS37781');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `main_campany`
--
ALTER TABLE `main_campany`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `main_campany`
--
ALTER TABLE `main_campany`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
