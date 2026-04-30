# 五位百法 - 逻辑关系图

此图展示了“一切法”如何展开为五位的逻辑过程。

```mermaid
graph TD
    Root[一切法<br/>All Dharmas]
    
    %% 第一层分判
    Root --> Samskrta[有为法<br/>Conditioned Dharmas]
    Root --> Asamskrta[无为法<br/>Unconditioned Dharmas]

    %% 有为法子图
    subgraph Conditioned [有为法 - 虚妄分别]
        direction TB
        Citta[1. 心法<br/>Mind]
        Caitasika[2. 心所法<br/>Mental Factors]
        Rupa[3. 色法<br/>Form]
        Viprayukta[4. 心不相应行法<br/>Non-associated]
        
        %% 逻辑连接
        Citta -- 最胜故<br/>(Supreme) --> Caitasika
        Citta & Caitasika -- 二所现影故<br/>(Manifested Image) --> Rupa
        Citta & Caitasika & Rupa -- 三位差别故<br/>(Distinction of Positions) --> Viprayukta
    end

    %% 无为法子图
    subgraph Unconditioned [无为法 - 真实体性]
        Asamskrta_Node[5. 无为法<br/>Unconditioned]
    end

    %% 最终连接
    Conditioned -- 四所显示故<br/>(Revealed by the four) --> Unconditioned

    %% 样式定义
    classDef root fill:#f9f,stroke:#333,stroke-width:4px;
    classDef mind fill:#e1f5fe,stroke:#01579b;
    classDef mental fill:#e8f5e9,stroke:#2e7d32;
    classDef form fill:#fff3e0,stroke:#ef6c00;
    classDef non fill:#f3e5f5,stroke:#7b1fa2;
    classDef void fill:#eceff1,stroke:#455a64;

    class Root root;
    class Citta mind;
    class Caitasika mental;
    class Rupa form;
    class Viprayukta non;
    class Asamskrta,Asamskrta_Node void;
```

## 逻辑说明

1.  **心法 (Mind)**: 在一切有为法中，心法起主导作用，如国王，故称“最胜”。
2.  **心所法 (Mental Factors)**: 恒常依随心法而起，如大臣随从国王，故称“与此相应”。
3.  **色法 (Form)**: 并非独立存在的实体，而是心与心所变现的影像，故称“二所现影”。
4.  **心不相应行法 (Non-associated)**: 既非色法也非心法，是在前三者的分位上假立的差别相，故称“三位差别”。
5.  **无为法 (Unconditioned)**: 前四种有为法灭除虚妄后所显示的真实理体，故称“四所显示”。
