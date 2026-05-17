import type { NextConfig } from "next";
import path from "node:path";

const nextConfig: NextConfig = {
  transpilePackages: ["@linguaflow/shared-core"],
  webpack: (config) => {
    config.resolve.alias["@linguaflow/shared-core"] = path.resolve(__dirname, "../packages/shared-core/src/index.ts");
    config.resolve.alias["@linguaflow/shared-core/hooks/adventure"] = path.resolve(__dirname, "../packages/shared-core/src/hooks/adventure/index.ts");
    config.resolve.alias["@linguaflow/shared-core/hooks/study"] = path.resolve(__dirname, "../packages/shared-core/src/hooks/study/index.ts");
    return config;
  },
};

export default nextConfig;
