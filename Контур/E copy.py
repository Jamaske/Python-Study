const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputLines = [];
rl.on('line', (line) => {
    inputLines.push(line);
});

rl.on('close', () => {
    const [N, M, q] = inputLines[0].split(' ').map(Number);

    const ships = [];
    const indexes = Array.from({ length: N }, () => Array(M).fill(-1));
    const grid = inputLines.slice(1, N + 1);
    const visited = Array.from({ length: N }, () => Array(M).fill(false));

    function dfs(x, y, shipId) {
        if (x < 0 || x >= M || y < 0 || y >= N || visited[y][x] || grid[y][x] === '.') {
            return;
        }

        visited[y][x] = true;
        indexes[y][x] = shipId;
        ships[shipId].add(`${x},${y}`);

        const directions = [
            [-1, 0], [1, 0],
            [0, -1], [0, 1]
        ];

        for (const [dx, dy] of directions) {
            dfs(x + dx, y + dy, shipId);
        }
    }

    function createShip(x, y) {
        if (grid[y][x] === 'X' && indexes[y][x] === -1) {
            const shipId = ships.length;
            ships.push(new Set());
            dfs(x, y, shipId);
        }
    }

    for (let y = 0; y < N; y++) {
        for (let x = 0; x < M; x++) {
            createShip(x, y);
        }
    }



    // Process each query
    for (let i = N + 1; i < N + 1 + q; i++) {
        const [y, x] = inputLines[i].split(' ').map(Number);

        const shipNum = indexes[y - 1][x - 1];
        if (shipNum === -1) {
            console.log("MISS");
            continue;
        }

        const ship = ships[shipNum];
        ship.delete(`${x - 1},${y - 1}`);

        if (ship.size === 0) {
            console.log("DESTROY");
        } else {
            console.log("HIT");
        }
    }
});
