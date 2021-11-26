import java.util.*;

class Solution {

    List<Node> nodes = new ArrayList<Node>();
    int max_length = 1;
    int temp_length = 1;

    public int largestComponentSize(int[] nums) {
        for (int i : nums) {
           nodes.add(new Node(i));
        }

        findNeighbours(nodes);
        DFS(nodes);
        return max_length;
    }

    public int findGCF(int num1, int num2) {
        int gcf = 1;

        for (int i = 1; i <= num1 && i <= num2; i++)
        {
            if(num1 % i == 0 && num2 % i == 0)
                gcf = i;
        }
        return gcf;
    }

    public void findNeighbours(List<Node> nodes) {
        for (Node node1 : nodes) {
            for (Node node2 : nodes){
                if (!node1.equals(node2)) {
                    if (findGCF(node1.getValue(), node2.getValue()) > 1) {
                        node1.addNeighbour(node2);
                    }
                }
            }
        }
    }

    public void DFS (List<Node> nodes) {
        boolean[] isVisited = new boolean[nodes.size()];
        for (int i = 0; i < isVisited.length; i++){
            if (!isVisited[i]) {
                temp_length = 1;
                dfsRecursive(nodes.get(i), isVisited);
                if (max_length < temp_length) {
                    max_length = temp_length;
                }
            }
        }
    }

    private void dfsRecursive(Node current, boolean[] isVisited) {
        isVisited[nodes.indexOf(current)] = true;

        for (Node dest : current.getNeighbours()) {
            if (!isVisited[nodes.indexOf(dest)]) {
                temp_length += 1;
                dfsRecursive(dest, isVisited);
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {1,6154,4113,6162,19,5465,4125,9221,6176,8229,4134,39,41,8234,6187,46,2097,50,54,4153,2106,8260,6213,4167,6223,6224,82,2132,8277,2137,8286,2150,118,5483,8328,4234,8334,2191,6289,2197,4246,1437,6310,173,8367,180,4284,7882,8389,2247,8397,4305,8403,6368,2288,242,4340,6389,2294,249,251,254,2307,6406,8459,4366,7215,286,287,296,6441,298,4395,4398,8502,314,8246,1761,8524,4431,6484,6201,1444,6510,4463,8562,2420,6519,386,392,2441,4491,4496,6549,8602,2466,425,6575,440,8643,4549,6603,8654,8655,4563,473,481,8676,6642,8692,8617,8703,6660,6665,6669,2575,530,533,8726,772,6684,8738,551,8745,554,8748,4190,4662,8761,2627,8774,2631,2633,8785,8786,6926,600,2651,4701,8812,4722,8819,8980,5567,2684,637,1813,4737,8844,8845,4752,2711,8858,6817,6939,6822,8871,4778,2733,6831,690,2741,694,699,703,4808,8908,717,720,8915,1146,6884,8936,6889,8940,6910,2817,4868,773,2830,784,788,4886,6938,8987,8991,2856,2861,2865,4914,819,9017,9019,4928,9027,9030,1847,2894,9045,7002,7006,7007,7015,4971,7020,7025,882,9083,898,7043,4996,9095,911,5009,915,7060,9109,918,5016,924,9126,2983,7083,7089,5046,7097,3002,3004,5060,3017,9719,3025,978,3027,3038,5090,7141,3053,1012,1020,1021,3071,7168,7173,7175,9233,1043,7190,7194,9244,3102,7200,5157,7207,3116,3117,9263,7219,4617,5176,4276,2911,5182,5183,5186,1091,5192,1099,7246,1116,7269,1126,7272,1139,1143,7290,9347,5252,7301,1158,9351,5269,7318,5271,3227,1181,3231,5280,1185,1188,5289,7338,3245,7360,1229,7375,5328,9427,3280,3299,3307,1260,3309,5360,7410,5364,3317,1271,9472,3329,3332,3333,7432,1291,9494,9497,3355,9512,7467,1339,3390,9535,3398,7495,5448,9783,9550,1364,7513,9564,7521,9574,3431,9576,7531,5495,9596,5502,8771,9620,1433,5530,3483,7581,3488,9633,7588,7589,1449,583,6386,1459,3515,9461,9667,4342,9677,2299,1515,3564,7663,5620,4347,1532,7679,3585,9730,7692,9816,1555,7707,9756,1567,8795,5668,3622,945,7721,1579,5677,3635,1591,5688,5696,1614,9807,3664,3665,5717,7767,1624,9818,3677,7775,1632,7780,1640,1642,5743,9832,5748,7804,9855,5760,1665,7812,3350,7814,9864,6764,3734,7833,5787,7837,5790,1697,1307,3754,9901,9908,5818,7868,1733,3786,1739,5836,9937,7890,9940,1752,3802,5852,3807,3809,5858,3817,5867,9965,5874,6783,1799,9992,7948,5901,5904,5905,3129,1820,1822,3879,3891,1673,1851,5956,1869,5974,5975,3931,1889,9531,3943,1903,3955,8053,6011,1916,1921,5782,6022,8074,3981,1937,1940,6044,1952,8097,6050,6051,8129,6086,4053,2008,6110,6112,4065,7165,2388};
        Solution solution = new Solution();
        System.out.println(solution.largestComponentSize(nums));
    }
}

class Node {

    private int value;
    private List<Node> neighbours = new ArrayList<Node>();

    public Node (int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public List<Node> getNeighbours() {
        return neighbours;
    }

    public void print_nodes(List<Node> nodes) {
        for (Node node : nodes) {
            System.out.print(node.getValue() + ",");
        }
        System.out.println();
    }


    public void setNeighbours(List<Node> neighbours) {
        this.neighbours = neighbours;
    }

    public void addNeighbour(Node node) {
        if(!neighbours.contains(node)) {
            neighbours.add(node);
        }
    }
}
