var Node = neataptic.Node;
var Neat = neataptic.Neat;
var Network = neataptic.Network;
var Methods = neataptic.methods;
var Architect = neataptic.architect;
var Trainer = neataptic.Trainer;

var network = Architect.Perceptron(2, 1, 4);

network.activate([0, 1]);
drawGraph(network.graph(1000, 1000), '.draw');