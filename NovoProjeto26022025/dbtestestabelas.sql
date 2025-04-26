-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 26-Fev-2025 às 16:48
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `dbtestestabelas`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

CREATE TABLE `produtos` (
  `Produto_Id` int(11) NOT NULL,
  `Produto_nome` varchar(100) DEFAULT NULL,
  `Produto_descrit` varchar(600) DEFAULT NULL,
  `Produto_preco` float DEFAULT NULL,
  `Produto_quantidade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `produtos`
--

INSERT INTO `produtos` (`Produto_Id`, `Produto_nome`, `Produto_descrit`, `Produto_preco`, `Produto_quantidade`) VALUES
(1, 'Rato SUBBLIM Smart 2.0', 'Este é o Rato SUBBLIM Smart, um dispositivo de navegação de alta qualidade que pode ser usado tanto por destros como por canhotos. Com uma resolução de 1600 dpi, este rato oferece um rastreamento preciso e suave, tornando a navegação mais confortável.', 17.49, 2147483647),
(2, 'Hot Spot 2KM Blue', 'Hot Spot Condomínio fechado 2KM', 399.99, 12),
(3, 'PC HP 400G6 AIO', 'Intel Core i5, Memória RAM_ 8 GB, Intel® UHD Graphics 630, Windows 10 Pro', 1046, 45),
(5, 'Smarphone Virtual NUNGKU', 'NUNGKU é a marca de criação de objetos virtuais em realidade aumentada', 3455, 12),
(6, 'Desktop XPTO AA2B', 'Pc gaming de última geração em que não precisas de pc, pois o pc é virtual', 12000, 3),
(7, 'Consola Playstation PS5 Slim Digital', 'Joga Como Nunca PlayStation®5 — edição digital Design slim\nCom a PS5®, os jogadores podem desfrutar de uma poderosa tecnologia de jogo num design de consola elegante e compacto. 1TB of Storage Mantém os teus títulos favoritos prontos a jogar com 1 TB de armazenamento SSD incorporado. SSD ultrarrápido Maximiza as tuas sessões de jogo com tempos de carregamento quase instantâneos para jogos PS5™ instalados. E/S integrado\nA integração personalizada dos sistemas da consola PS5™ permite aos criadores obter dados do SSD tão rapidamente que conseguem criar jogos de formas nunca antes possíveis. Ray T', 374, 6),
(8, 'Smartphone Samsung Galaxy A35 5G - 128 GB - Lilás', 'Capta as melhores fotografias com a câmara grandeangular de alta resolução de 50MP. As cores vivas e os detalhes vão deixar as tuas fotos incríveis e prontas para serem partilhadas!\nConsegue fotografias mais nítidas e melhor visibilidade mesmo no escuro com a Nightography. Com um desempenho NPU mehorado e um sensor otimizado,\nconsegue mais detalhes em cada fotografia.\nO Galay A35 5G apresenta também vídeos em Super HDR para obter cores vivas, vídeos nítidos e melhor visibilidade mesmo em diferentes condições de iluminação. Grava\nmovimentos precisos e suaves com o estabilizador VDIS em 4K.', 328.99, 7),
(10, 'Projetor portátil Gaimoo', '[App integrada] Projetor 1080P FHD 4K Supote 2024 Upgraded Projetor portátil de controlo duplo com rato Android TV WiFi 6 BT5.2 180° Rotação HDMI/TV Stick/USB/PS5/Laptop, com cabo HDMI e rato, BB', 88.99, 12),
(11, 'Smartphone SAMSUNG Galaxy S24', 'Conheça o Galaxy S24 e S24 Plus, a excelência em tecnologia com o smartphone líder em câmara, desempenho incomparável e Galaxy AI. Simplesmente épico.', 799, 5),
(12, 'Play Hit', 'Jogos de tabuleiro para adultos divertidos e dinâmicos - música em espanhol - diversão com amigos e família - presente de Natal original para homens e mulheres', 23, 3),
(13, 'Rato Realidade Aumenta', 'Este é um produto inovador, para quê ter o objeto fisico, se podemos ter virtualmente', 2000, 12),
(14, 'Tijolo', 'testes', 12, 12);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`Produto_Id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `produtos`
--
ALTER TABLE `produtos`
  MODIFY `Produto_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
