-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 22, 2023 at 06:05 AM
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
-- Table structure for table `main_network`
--

CREATE TABLE `main_network` (
  `id` bigint NOT NULL,
  `state` varchar(50) NOT NULL,
  `network` varchar(50) NOT NULL,
  `time` date NOT NULL,
  `description` varchar(500) NOT NULL,
  `compony_info_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_network`
--

INSERT INTO `main_network` (`id`, `state`, `network`, `time`, `description`, `compony_info_id`) VALUES
(1, 'O', '154.115.200.0/24', '2023-05-21', 'Telesom', 1),
(2, 'O', '154.115.216.0/22', '2023-05-21', 'TELESOM CLOUD SERVICES', 1),
(3, 'O', '154.115.220.0/22', '2023-05-21', 'MBB INTERNET', 1),
(4, 'O', '154.115.225.0/24', '2023-05-21', 'LAAS-MBB', 1),
(5, 'O', '154.115.227.0/24', '2023-05-21', 'Telesom', 1),
(6, 'O', '154.115.230.0/24', '2023-05-21', 'Telesom', 1),
(7, 'O', '154.115.240.0/24', '2023-05-21', 'TELESOM', 1),
(8, 'O', '154.115.242.0/23', '2023-05-21', 'Telesom', 1),
(9, 'O', '154.115.244.0/23', '2023-05-21', 'Telesom', 1),
(10, 'O', '154.115.245.0/24', '2023-05-21', 'Telesom', 1),
(11, 'O', '154.115.246.0/24', '2023-05-21', 'BORAMA INTERNET', 1),
(12, 'O', '154.115.247.0/24', '2023-05-21', 'TELESOM', 1),
(13, 'O', '154.115.248.0/24', '2023-05-21', 'TELESOM', 1),
(14, 'O', '154.115.250.0/24', '2023-05-21', 'TELESOM', 1),
(15, 'O', '154.115.251.0/24', '2023-05-21', 'TELESOM', 1),
(16, 'O', '154.115.252.0/23', '2023-05-21', 'TELESOM	', 1),
(17, 'O', '154.115.254.0/24', '2023-05-21', 'LASANOD INTERNET	', 1),
(18, 'O', '154.115.255.0/24', '2023-05-21', 'LASANOD INTERNTE	', 1),
(19, 'O', '197.157.244.0/24', '2023-05-21', 'VOIP Interconnections	', 1),
(20, 'O', '197.157.245.0/24', '2023-05-21', 'IP Pool for Subscribers that are on Ethiotelecom Link which are behind a NAT	', 1),
(21, 'O', '197.157.246.0/24', '2023-05-21', 'Telesom', 1),
(22, 'O', '197.220.64.0/24', '2023-05-21', 'public assignment', 2),
(23, 'O', '197.220.65.0/24', '2023-05-21', 'public assignment	', 2),
(24, 'O', '197.220.66.0/24', '2023-05-21', 'public assignment', 2),
(25, 'O', '197.220.67.0/24', '2023-05-21', 'public assignment', 2),
(26, 'O', '197.220.68.0/24', '2023-05-21', 'public assignment', 2),
(27, 'O', '197.220.69.0/24', '2023-05-21', 'public assignment', 2),
(28, 'O', '197.220.70.0/24', '2023-05-21', 'public assignment', 2),
(29, 'O', '197.220.71.0/24', '2023-05-21', 'public assignment', 2),
(30, 'O', '197.220.72.0/24', '2023-05-21', 'public assignment', 2),
(31, 'O', '197.220.73.0/24', '2023-05-21', 'public assignment', 2),
(32, 'O', '197.220.74.0/24', '2023-05-21', 'public assignment', 2),
(33, 'O', '197.220.75.0/24', '2023-05-21', 'public assignment', 2),
(34, 'O', '197.220.76.0/24', '2023-05-21', 'public assignment', 2),
(35, 'O', '197.220.77.0/24', '2023-05-21', 'public assignment', 2),
(36, 'O', '197.220.78.0/24', '2023-05-21', 'public assignment', 2),
(37, 'O', '197.220.79.0/24', '2023-05-21', 'public assignment', 2),
(38, 'O', '197.220.80.0/24', '2023-05-21', 'public assignment', 2),
(39, 'O', '192.145.168.0/24', '2023-05-21', 'Hormuud Telecom Somalia INC	', 3),
(40, 'O', '192.145.169.0/24', '2023-05-21', 'Hormuud Telecom Somalia INC	', 3),
(41, 'O', '192.145.170.0/24', '2023-05-21', 'Hormuud Telecom Somalia INC	', 3),
(42, 'O', '192.145.171.0/24', '2023-05-21', 'Hormuud Telecom Somalia INC	', 3),
(43, 'O', '192.145.172.0/24', '2023-05-21', 'Hormuud Telecom Somalia INC	', 3),
(44, 'O', '192.145.173.0/24', '2023-05-21', 'Hormuud Telecom Somalia INC', 3),
(45, 'O', '192.145.174.0/24', '2023-05-21', 'Hormuud Telecom Somalia INC	', 3),
(46, 'O', '192.145.175.0/24', '2023-05-21', 'Hormuud Telecom Somalia INC	', 3),
(47, 'O', '197.220.84.0/24', '2023-05-21', 'public assignment	', 3),
(48, 'O', '197.220.88.0/24', '2023-05-21', 'public assignment	', 3),
(49, 'O', '197.220.89.0/24', '2023-05-21', 'public assignment	', 3),
(50, 'O', '197.220.90.0/24', '2023-05-21', 'public assignment	', 3),
(51, 'O', '197.220.91.0/24', '2023-05-21', 'public assignment	', 3),
(52, 'O', '41.78.72.0/24', '2023-05-21', 'Hormuud-Telecom-Somalia-inc	', 3),
(53, 'O', '41.78.73.0/24', '2023-05-21', 'Hormuud Telecom Somalia	', 3),
(54, 'O', '41.78.74.0/24', '2023-05-21', 'Hormuud Telecom Somalia	', 3),
(55, 'O', '41.78.75.0/24', '2023-05-21', 'Hormuud-Telecom-Somalia-inc	', 3),
(56, 'O', '102.220.40.0/24', '2023-05-21', 'The above subnet assigned to A customer Dera internet connection', 4),
(57, 'O', '102.220.41.0/24', '2023-05-21', 'The above IP addresses assigned to customer	', 4),
(58, 'O', '102.220.42.0/24', '2023-05-21', 'The above IP addresses assigned to customer	', 4),
(59, 'O', '102.220.43.0/24', '2023-05-21', 'The above IP addresses assigned to customer', 4),
(60, 'O', '102.223.188.0/24', '2023-05-21', 'Golis Telecom Somalia', 4),
(61, 'O', '102.223.189.0/24', '2023-05-21', 'Golis Telecom Somalia', 4),
(62, 'O', '102.223.190.0/24', '2023-05-21', 'Golis Telecom Somalia', 4),
(63, 'O', '102.223.191.0/24', '2023-05-21', 'Golis Telecom Somalia', 4),
(64, 'O', '41.223.108.0/24', '2023-05-21', 'Above IP address we assigned the customers', 4),
(65, 'O', '41.223.109.0/24', '2023-05-21', 'The above IP address we allocated our systems for connectivity	', 4),
(66, 'O', '41.223.111.0/24', '2023-05-21', 'for the above IPv4 we are using for google and facebook peering', 4),
(67, 'O', '102.128.128.0/24', '2023-05-21', 'Somtel-4G	', 5),
(68, 'O', '102.128.129.0/24', '2023-05-21', 'SOMTEL INTERNATIONAL Ltd', 5),
(69, 'O', '102.128.130.0/24', '2023-05-21', 'SOMTEL INTERNATIONAL Ltd', 5),
(70, 'O', '102.128.131.0/24', '2023-05-21', 'SOMTEL INTERNATIONAL Ltd', 5),
(71, 'O', '102.128.132.0/24', '2023-05-21', 'SOMTEL INTERNATIONAL Ltd', 5),
(72, 'O', '102.128.133.0/24', '2023-05-21', 'SOMTEL INTERNATIONAL Ltd	', 5),
(73, 'O', '197.231.200.0/24', '2023-05-21', 'Somtel-Somaliland	', 5),
(74, 'O', '197.231.201.0/24', '2023-05-21', 'Somtel-IT', 5),
(75, 'O', '197.231.202.0/24', '2023-05-21', 'Somtel-4G-Hargeisa', 5),
(76, 'O', '197.231.203.0/24', '2023-05-21', 'Somtel-SL-West', 5),
(77, 'O', '102.68.144.0/21', '2023-05-21', 'Economic & Strategic Research Center', 6),
(78, 'O', '102.214.168.0/24', '2023-05-21', 'SOMTEL SOMALIA LTD	', 7),
(79, 'O', '102.214.169.0/24', '2023-05-21', '102.214.169.0 - 102.214.169.255', 7),
(80, 'O', '102.68.16.0/24', '2023-05-21', 'Somtel Somalia LTD	', 7),
(81, 'O', '102.68.17.0/24', '2023-05-21', 'Somtel Somalia LTD', 7),
(82, 'O', '102.68.18.0/24', '2023-05-21', 'Somtel Somalia LTD	', 7),
(83, 'O', '102.68.19.0/24', '2023-05-21', 'Somtel Somalia LTD	', 7),
(84, 'O', '41.79.196.0/22', '2023-05-21', 'SomCable', 8),
(85, 'O', '154.73.24.0/24', '2023-05-21', 'This is block is used to connect the P2P links connected to the second ISP.	', 9),
(86, 'O', '154.73.25.0/24', '2023-05-21', 'This block is used for the SomaliREN servers and services	', 9),
(87, 'O', '154.73.26.0/24', '2023-05-21', 'This block is used to connect our P2P links connected to our first ISP UbuntuNet Alliance.	', 9),
(88, 'O', '154.73.27.0/24', '2023-05-21', 'This block is assigned our member institutions to host some of their criticl services and its devided into /27s for each institituins.	', 9),
(89, 'O', '154.73.44.0/22', '2023-05-21', 'Somcast Networks LLC	', 10),
(90, 'O', '154.118.240.0/24', '2023-05-22', 'Somali Optical Networks	', 11),
(91, 'O', '154.118.241.0/24', '2023-05-22', 'Somali Optical Networks	', 11),
(92, 'O', '154.118.242.0/24', '2023-05-22', 'SOON SAHAL PUBLIC IPS	', 11),
(93, 'O', '154.118.243.0/24', '2023-05-22', 'SOON MI MOPT IPS	', 11),
(94, 'O', '154.73.124.0/22', '2023-05-22', 'Sahal Telecom Somalia	', 12),
(95, 'O', '102.38.48.0/22', '2023-05-22', 'Somlink Wireless Network	', 13),
(96, 'O', '102.218.56.0/22', '2023-05-22', 'SO! Limited	', 14),
(97, 'O', '154.72.24.0/24', '2023-05-22', 'Fixed Line Customers	', 15),
(98, 'O', '154.72.25.0/24', '2023-05-22', 'Somali Wireless	', 15),
(99, 'O', '154.72.27.0/24', '2023-05-22', 'Somalia Wireless	', 15),
(100, 'O', '102.141.196.0/24', '2023-05-22', 'AMTEL LTD	', 16),
(101, 'O', '102.141.197.0/24', '2023-05-22', 'AMTEL LTD	', 16),
(102, 'O', '102.141.198.0/24', '2023-05-22', 'AMTEL LTD	', 16),
(103, 'O', '102.218.10.0/23', '2023-05-22', 'Bluecom Ltd	', 17),
(104, 'O', '102.218.98.0/24', '2023-05-22', 'TAYOCOM	', 18),
(105, 'O', '196.11.62.0/24', '2023-05-22', 'Ministry of Posts, Telecommunications and Technology	', 19),
(106, 'O', '154.72.48.0/24', '2023-05-22', 'Dalkom Somalia	', 20),
(107, 'O', '154.72.50.0/24', '2023-05-22', 'Dalkom Somalia	', 20),
(108, 'O', '154.72.51.0/24', '2023-05-22', 'Dalkom Somalia	', 20);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `main_network`
--
ALTER TABLE `main_network`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_network_compony_info_id_c00e8d65_fk_main_campany_id` (`compony_info_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `main_network`
--
ALTER TABLE `main_network`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=136;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `main_network`
--
ALTER TABLE `main_network`
  ADD CONSTRAINT `main_network_compony_info_id_c00e8d65_fk_main_campany_id` FOREIGN KEY (`compony_info_id`) REFERENCES `main_campany` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
